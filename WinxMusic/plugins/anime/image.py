from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from requests import get

from WinxMusic import app


@app.on_message(
    filters.command(["image"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
)
async def pinterest(_, message):
    chat_id = message.chat.id

    try:
        query = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply("➜ precisa de um texto para pesquisa 🔍")

    images = get(f"https://pinterest-api-one.vercel.app/?q={query}").json()

    media_group = []
    count = 0

    msg = await message.reply(f"➜ pesquisando por {query}")
    for url in images["images"][:6]:
        media_group.append(InputMediaPhoto(media=url))
        count += 1
        await msg.edit(
            f"➜ pesquisando por {query} \n➜ {count} de 6 imagens encontradas"
        )

    try:
        await app.send_media_group(
            chat_id=chat_id, media=media_group, reply_to_message_id=message.id
        )
        return await msg.delete()

    except Exception as e:
        await msg.delete()
        return await message.reply(f"erro: {e}")
