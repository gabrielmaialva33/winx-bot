import os

from pyrogram import filters

from WinxMusic import app
from WinxMusic.helpers.lexica_api import upscale_image
from WinxMusic.helpers.misc import get_file

UPSCALE_COMMAND = ["upscale", "aumentar", "aumente", "melhorar", "melhore"]


@app.on_message(filters.command(UPSCALE_COMMAND) & filters.group)
async def upscale(_, message):
    file = await get_file(message)
    if file is None:
        return await message.reply_text(
            "💬 ➜ responda a uma mensagem com uma 🖼️ para 🔍 aumentar a escala ⬆️."
        )

    msg = await message.reply_text("<code>➜ ⏳ampliando a imagem... 💭</code>")
    try:
        with open(file, "rb") as image_file:
            imageBytes = image_file.read()

        upscaled = await upscale_image(imageBytes)

        with open(upscaled, "rb") as upscaled_file:
            await message.reply_document(
                upscaled_file,
                caption=f"<code>➜ 🖼️ imagem ampliada com sucesso! ⬆️</code>",
            )

        await msg.delete()
    except Exception as e:
        await msg.edit(f"➜ ❌ erro ao 🔍 ampliar a imagem 😕: {e}")
    finally:
        if os.path.exists(file):
            os.remove(file)
        if os.path.exists(upscaled):
            os.remove(upscaled)
