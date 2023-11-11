from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaDocument,
    Message,
)

import config
from WinxMusic import LOGGER, app
from WinxMusic.helpers.lexica_api import ImageGeneration
from WinxMusic.helpers.misc import ImageModels, getText

PromptDB = {}


@app.on_message(filters.command(["draw", "desenhar", "desenhe"], prefixes=["/", "!"]))
async def generate(_, message: Message):
    global PromptDB
    prompt = await getText(message)
    if prompt is None:
        return await message.reply_text("➜ você não me deu um prompt para desenhar!")
    user = message.from_user
    btns = []
    PromptDB[user.id] = {"prompt": prompt, "reply_to_id": message.id}
    for i in ImageModels:
        btns.append(
            InlineKeyboardButton(
                text=i, callback_data=f"draw.{ImageModels[i]}.{user.id}"
            )
        )
    btns = [
        [btns[0], btns[1]],
        [btns[2], btns[3]],
        [btns[4], btns[5]],
        [btns[6], btns[7]],
        [btns[8], btns[9]],
        [btns[10], btns[11]],
        [btns[12], btns[13]],
    ]
    await message.reply_animation(
        config.GLOBAL_IMG_URL,
        caption=f"➜ Escolha um modelo",
        reply_markup=InlineKeyboardMarkup(btns),
    )


@app.on_callback_query(filters.regex("^draw.(.*)"))
async def draw(_, query):
    data = query.data.split(".")
    auth_user = int(data[-1])
    if query.from_user.id != auth_user:
        return await query.answer("Não é seu pedido!", show_alert=True)
    promptdata = PromptDB.get(auth_user, None)
    if promptdata is None:
        return await query.edit_message_text(
            "algo deu errado, tente novamente mais tarde"
        )
    await query.edit_message_text("➜ desenhando...")

    try:
        img_url = await ImageGeneration(int(data[1]), promptdata["prompt"])
        if img_url is None or img_url == 2 or img_url == 1:
            return await query.edit_message_text(
                "algo deu errado, tente novamente mais tarde"
            )
        images = []
        await query.message.delete()
        del PromptDB[auth_user]
        for i in img_url:
            images.append(
                InputMediaDocument(
                    i,
                    caption=f"➜ prompt: {promptdata['prompt']}\n\npoe: @{app.me.username}",
                )
            )

        await app.send_media_group(
            chat_id=query.message.chat.id,
            media=images,
            reply_to_message_id=promptdata["reply_to_id"],
        )
    except Exception as e:
        LOGGER(__name__).error(e)
        await query.message.delete()
