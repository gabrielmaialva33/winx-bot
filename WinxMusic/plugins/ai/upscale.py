import os

from pyrogram import filters

from WinxMusic import app
from WinxMusic.helpers.lexica_api import UpscaleImages
from WinxMusic.helpers.misc import getFile


@app.on_message(filters.command("upscale"))
async def upscaleImages(_, message):
    file = await getFile(message)
    if file is None:
        return await message.reply_text("Respondeu a uma imagem?")
    msg = await message.reply("Espere um pouco...")
    try:
        imageBytes = open(file, "rb").read()
        os.remove(file)
        upscaledImage = await UpscaleImages(imageBytes)
        await message.reply_document(
            open(upscaledImage, "rb"), caption=f"Upscaled poe @{app.me.username}"
        )
        await msg.delete()
        os.remove(upscaledImage)
    except Exception as e:
        await msg.edit(f"{e}")
