from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument, Message
from WinxMusic import LOGGER, app
from WinxMusic.helpers.lexica_api import ImageGeneration
from WinxMusic.helpers.misc import ImageModels, getText
from config import BANNED_USERS

# É recomendado usar uma alternativa para substituir essa variável global
prompt_db = {}

# Constantes para mensagens
PROMPT_MISSING_MSG = "➜ você não me deu um prompt para desenhar!"
CHOOSE_MODEL_MSG = "➜ Escolha um modelo"
ERROR_MSG = "➜ algo deu errado, tente novamente mais tarde"
DRAWING_MSG = "➜ desenhando..."
NOT_YOUR_REQUEST_MSG = "➜ não é seu pedido!"


@app.on_message(filters.command(["draw", "desenhar", "desenhe"], prefixes=["/", "!"]) & filters.group & ~BANNED_USERS)
async def generate(_, message: Message):
    prompt = await getText(message)
    if prompt is None:
        return await message.reply_text(PROMPT_MISSING_MSG)

    user = message.from_user
    prompt_db[user.id] = {"prompt": prompt, "reply_to_id": message.id}
    btns = generate_buttons(user.id)

    await message.reply_animation(config.GLOBAL_IMG_URL, caption=CHOOSE_MODEL_MSG, reply_markup=InlineKeyboardMarkup(btns))


def generate_buttons(user_id):
    buttons = [InlineKeyboardButton(text=model, callback_data=f"draw.{ImageModels[model]}.{user_id}") for model in ImageModels]
    return [buttons[i:i + 2] for i in range(0, len(buttons), 2)]


@app.on_callback_query(filters.regex("^draw.(.*)"))
async def draw(_, query):
    data = query.data.split(".")
    auth_user = int(data[-1])

    if query.from_user.id != auth_user:
        return await query.answer(NOT_YOUR_REQUEST_MSG, show_alert=True)

    prompt_data = prompt_db.get(auth_user)
    if prompt_data is None:
        return await query.edit_message_text(ERROR_MSG)

    await query.edit_message_text(DRAWING_MSG)
    await process_drawing(query, data[1], prompt_data)


async def process_drawing(query, model_id, prompt_data):
    try:
        img_url = await ImageGeneration(int(model_id), prompt_data["prompt"])
        if img_url in [None, 1, 2]:
            return await query.edit_message_text(ERROR_MSG)

        images = [InputMediaDocument(url, caption=f"➜ prompt: {prompt_data['prompt']}\n\npoe: @{app.me.username}") for url in img_url]
        await app.send_media_group(chat_id=query.message.chat.id, media=images, reply_to_message_id=prompt_data["reply_to_id"])
        del prompt_db[query.from_user.id]
    except Exception as e:
        LOGGER(__name__).error(e)
        await query.message.reply_text(ERROR_MSG)
    finally:
        await query.message.delete()
