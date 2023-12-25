import aiohttp
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BANNED_USERS
from WinxMusic import app
from WinxMusic.helpers.misc import ChatModels, get_text

API_URL = "https://api.qewertyy.me/models"
API_TIMEOUT = 30

PROMPT_MISSING_MSG = "➜ você não me deu um prompt para gerar texto!"
CHOOSE_MODEL_MSG = "➜ Escolha um modelo de texto"
ERROR_MSG = "➜ algo deu errado, tente novamente mais tarde"
GENERATING_MSG = "➜ gerando resposta..."
NOT_YOUR_REQUEST_MSG = "➜ não é seu pedido!"

prompt_db = {}


@app.on_message(
    filters.command(["gpt"], prefixes=["/", "!"]) & filters.group & ~BANNED_USERS
)
async def generate_text(_, message: Message):
    prompt = await get_text(message)
    if prompt is None:
        return await message.reply_text(PROMPT_MISSING_MSG)

    user = message.from_user
    prompt_db[user.id] = {"prompt": prompt, "reply_to_id": message.id}
    btns = generate_text_buttons(user.id)

    await message.reply_text(
        CHOOSE_MODEL_MSG,
        reply_markup=InlineKeyboardMarkup(btns),
    )


def generate_text_buttons(user_id):
    buttons = [
        InlineKeyboardButton(
            text=model, callback_data=f"text.{ChatModels[model]}.{user_id}"
        )
        for model in ChatModels
    ]
    return [buttons[i : i + 2] for i in range(0, len(buttons), 2)]


@app.on_callback_query(filters.regex("^text.(.*)"))
async def generate_response(_, query):
    data = query.data.split(".")
    auth_user = int(data[-1])

    if query.from_user.id != auth_user:
        return await query.answer(NOT_YOUR_REQUEST_MSG, show_alert=True)

    prompt_data = prompt_db.get(auth_user)
    if prompt_data is None:
        return await query.edit_message_text(ERROR_MSG)

    await query.edit_message_text(GENERATING_MSG)
    await process_text_generation(query, data[1], prompt_data)


async def process_text_generation(query, model_id, prompt_data):
    try:
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=API_TIMEOUT)
        ) as session:
            api_params = {"model_id": model_id, "prompt": prompt_data["prompt"]}

            text_response = await get_chat_response(session, api_params)
            if text_response in [None, "error"]:
                return await query.edit_message_text(ERROR_MSG)

            await query.message.reply_text(
                text_response,
                reply_to_message_id=prompt_data["reply_to_id"],
            )
            del prompt_db[query.from_user.id]
    except Exception as e:
        await query.message.reply_text(ERROR_MSG)
    finally:
        await query.message.delete()


async def get_chat_response(session, api_params):
    async with session.post(API_URL, json=api_params) as response:
        if response.status == 200:
            data = await response.json()
            return data.get("content", "error: api retornou um valor nulo")

        else:
            return f"error: api retornou {response.status} status code"