from lexica import AsyncClient, languageModels
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from WinxMusic.utils import get_lang
from config import BANNED_USERS
from WinxMusic import LOGGER, app
from WinxMusic.helpers.misc import get_text
from strings import get_string

prompt_db = {}
models = {getattr(languageModels, attr).get("name"): getattr(languageModels, attr).get("modelId")
          for attr in dir(languageModels)
          if not attr.startswith("__") and isinstance(getattr(languageModels, attr), dict)}


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
    prompt_db[user.id] = {"prompt": prompt, "reply_to_id": message.id, "user": user}
    buttons = generate_text_buttons(user.id)

    await message.reply_text(
        _["llm_2"],
        reply_markup=InlineKeyboardMarkup(buttons),
    )


# class languageModels(object):
#     bard = {"modelId":20,"name":"Bard"}
#     palm = {"modelId":0,"name":"PaLM"}
#     palm2 = {"modelId":1,"name":"PaLM 2"}
#     mistral = {"modelId":21,"name":"LLAMA 2"}
#     llama = {"modelId":18,"name":"LLAMA"}
#     gpt = {"modelId":5,"name":"ChatGPT"}
#     gemini = {"modelId":23,"name":"Gemini-Pro"}
#     geminiVision = {"modelId":24,"name":"Gemini-Pro-Vision"}
#     openhermes = {"modelId":27,"name":"OpenHermes"}
def generate_text_buttons(user_id):
    buttons = [
        InlineKeyboardButton(
            text=model, callback_data=f"llm_{user_id}_{model_id}"
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
    model_name = data[2]

    prompt = prompt_db[user_id]["prompt"]
    client = AsyncClient()

    if callback_query.from_user.id != user_id:
        return await callback_query.answer(_["llm_3"], show_alert=True)

    model_attr = None
    for attr in dir(languageModels):
        if attr.startswith("__"):
            continue
        model_info = getattr(languageModels, attr)
        if model_info.get("name") == model_name:  # Compara o nome do modelo
            model_attr = model_info
            break

    if not model_attr:
        LOGGER(__name__).warning(f"Model not found: {model_name}")
        return await callback_query.message.edit_text(_["llm_4"])

    # try:
        response = await client.ChatCompletion(prompt, model_attr)
        if response is None:
            return await callback_query.edit_message_text(_["llm_4"])

        text = f"🌟<b>Modelo:</b> <code>{model_name}</code>🌟\n\n 💬<b>Resposta:</b> <i>{response}</i>💬"
        await callback_query.message.reply_text(
            text,
            reply_to_message_id=prompt_db[user_id]["reply_to_id"],
            parse_mode="html",
        )
    # except Exception as e:
    #     LOGGER(__name__).warning(str(e))
    #     return await callback_query.message.edit_text(_["llm_4"])
    # finally:
    #     await client.close()

