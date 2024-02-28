from lexica.constants import languageModels
from pyrogram import Client, filters
from pyrogram import types as t

from WinxMusic import app
from WinxMusic.helpers.lexica_api import lexica_chat_completion, lexica_gemini_vision
from WinxMusic.helpers.lexica_miscs import get_media, get_text


@app.on_message(
    filters.command([i for i in dir(languageModels) if not i.startswith("__")])
)
async def chatbots(_: Client, m: t.Message):
    prompt = get_text(m)
    media = get_media(m)
    if media is not None:
        return await ask_about_image(_, m, [media], prompt)
    if prompt is None:
        return await m.reply_text("Oie, como posso te ajudar?")
    model = m.command[0].lower()
    output = await lexica_chat_completion(prompt, model)
    if model == "bard":
        output, images = output
        if len(images) == 0:
            return await m.reply_text(output)
        media = []
        for i in images:
            media.append(t.InputMediaPhoto(i))
        media[0] = t.InputMediaPhoto(images[0], caption=output)
        await _.send_media_group(m.chat.id, media, reply_to_message_id=m.id)
        return
    await m.reply_text(output["parts"][0]["text"] if model == "gemini" else output)


async def ask_about_image(_: Client, m: t.Message, media_files: list, prompt: str):
    images = []
    for media in media_files:
        image = await _.download_media(
            media.file_id, file_name=f"./downloads/{m.from_user.id}_ask.jpg"
        )
        images.append(image)
    output = await lexica_gemini_vision(
        prompt if prompt else "o que é isso?", "geminiVision", images
    )
    await m.reply_text(output)
