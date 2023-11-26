import os

from pyrogram import filters

from WinxMusic import app
from WinxMusic.helpers.lexica_api import UpscaleImages
from WinxMusic.helpers.misc import getFile

UPSCALE_COMMAND = ["upscale", "aumentar", "aumente", "melhorar", "melhore"]


@app.on_message(filters.command(UPSCALE_COMMAND) & filters.group)
async def upscale(_, message):
    file = await getFile(message)
    if file is None:
        return await message.reply_text(
            "💬 ➜ responda a uma mensagem com uma 🖼️ para 🔍 aumentar a escala ⬆️."
        )

    msg = await message.reply_text("<code>➜ ⏳ampliando a imagem... 💭</code>")
    try:
        with open(file, "rb") as image_file:
            imageBytes = image_file.read()

        upscaled = await UpscaleImages(imageBytes)

        with open(upscaled, "rb") as upscaled_file:
            await message.reply_document(
                upscaled_file,
                caption=f" ➜ 🖼 imagem ampliada por 👤 @{app.me.username} ✅",
            )

        await msg.delete()
    except Exception as e:
        await msg.edit(f"➜ ❌ erro ao 🔍 ampliar a 🖼️ imagem 😕: {e}")
    finally:
        if os.path.exists(file):
            os.remove(file)
        if os.path.exists(upscaled):
            os.remove(upscaled)
