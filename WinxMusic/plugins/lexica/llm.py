from lexica import AsyncClient, languageModels
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from WinxMusic import LOGGER, app
from WinxMusic.helpers.misc import get_text
from WinxMusic.utils import get_lang
from config import BANNED_USERS
from strings import get_string

main_prompt = "Você é a AI do Clube das Winx(Grupo Telegram). Ao responder, por favor, chame o usuário pelo nome. {0}"
prompt_db = {}
models = {getattr(languageModels, attr).get("name"): getattr(languageModels, attr).get("modelId")
          for attr in dir(languageModels)
          if not attr.startswith("__") and isinstance(getattr(languageModels, attr), dict)}


def build_model_mapping():
    mapping = {}
    for attr_name in dir(languageModels):
        if not attr_name.startswith("__") and isinstance(getattr(languageModels, attr_name), dict):
            model_attr = getattr(languageModels, attr_name)
            mapping[model_attr['name']] = model_attr
    return mapping


model_mapping = build_model_mapping()


@app.on_message(
    filters.command(["llm"], prefixes=["/", "!"]) & filters.group & ~BANNED_USERS
)
async def llm(_client, message: Message):
    chat_id = message.chat.id
    language = await get_lang(chat_id)
    _ = get_string(language)

    prompt = await get_text(message)
    if prompt is None:
        return await message.reply_text(_["llm_1"])

    user = message.from_user
    prompt_db[user.id] = {"prompt": prompt, "reply_to_id": message.id, "user_name": user.first_name}
    buttons = generate_text_buttons(user.id)

    await message.reply_text(
        _["llm_2"],
        reply_markup=InlineKeyboardMarkup(buttons),
    )


def generate_text_buttons(user_id):
    buttons = [
        InlineKeyboardButton(
            text=model, callback_data=f"llm_{user_id}_{model_id}_{model}"
        )
        for model, model_id in models.items()
    ]

    return [buttons[i: i + 2] for i in range(0, len(buttons), 2)]


@app.on_callback_query(filters.regex(r"^llm_") & ~BANNED_USERS)
async def llm_callback(_client, callback_query):
    chat_id = callback_query.message.chat.id
    language = await get_lang(chat_id)
    _ = get_string(language)

    data = callback_query.data.split("_")
    user_id = int(data[1])
    model_object = model_mapping.get(data[3])

    prompt = prompt_db[user_id]["prompt"]
    client = AsyncClient()

    prepare_prompt = main_prompt.format(prompt_db[user_id]["user_name"]) + prompt

    if callback_query.from_user.id != user_id:
        return await callback_query.answer(_["llm_3"], show_alert=True)

    try:
        response = await client.ChatCompletion(prepare_prompt, model_object)
        if response["code"] != 2:
            return await callback_query.message.reply_text(_["llm_4"])

        response_text = response["content"]
        await callback_query.message.reply_text(response_text,
                                                reply_to_message_id=prompt_db[user_id]["reply_to_id"])
    except Exception as e:
        LOGGER(__name__).warning(str(e))
        await callback_query.message.reply_text(_["llm_4"])
    finally:
        await callback_query.message.delete()


@app.on_message(
    filters.command(["gpt"], prefixes=["/", "!"]) & filters.group & ~BANNED_USERS
)
async def gpt(_client, message: Message):
    chat_id = message.chat.id
    language = await get_lang(chat_id)
    _ = get_string(language)

    prompt = await get_text(message)
    if prompt is None:
        return await message.reply_text(_["llm_1"])

    user = message.from_user
    prompt_db[user.id] = {"prompt": prompt, "reply_to_id": message.id, "user_name": user.first_name}

    try:
        client = AsyncClient()
        response = await client.ChatCompletion(prompt, languageModels.gpt)
        if response["code"] != 2:
            return await message.reply_text(_["llm_4"])

        response_text = response["content"]

        await message.reply_text(response_text, reply_to_message_id=prompt_db[user.id]["reply_to_id"])
    except Exception as e:
        LOGGER(__name__).warning(str(e))
        await message.reply_text(_["llm_4"])


@app.on_message(
    filters.command(["bard"], prefixes=["/", "!"]) & filters.group & ~BANNED_USERS
)
async def bard(_client, message: Message):
    chat_id = message.chat.id
    language = await get_lang(chat_id)
    _ = get_string(language)

    prompt = await get_text(message)
    if prompt is None:
        return await message.reply_text(_["llm_1"])

    user = message.from_user
    prompt_db[user.id] = {"prompt": prompt, "reply_to_id": message.id, "user_name": user.first_name}

    try:
        client = AsyncClient()
        response = await client.ChatCompletion(prompt, languageModels.bard)
        if response["code"] != 2:
            return await message.reply_text(_["llm_4"])

        response_text = response["content"]

        await message.reply_text(response_text, reply_to_message_id=prompt_db[user.id]["reply_to_id"])
    except Exception as e:
        LOGGER(__name__).warning(str(e))
        await message.reply_text(_["llm_4"])
