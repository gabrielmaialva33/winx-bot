from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from requests import get
from WinxMusic import app


@app.on_message(filters.command(["image"], prefixes=["/", "!"]) & filters.group)
async def pinterest(_, message):
    try:
        # Obtendo a consulta do usuário
        query = message.text.split(None, 1)[1]
    except IndexError:
        # Mensagem de erro se não houver consulta
        return await message.reply("➜ informe um texto para pesquisa 🔍")

    # Solicitando imagens da API
    response = get(f"https://pinterest-api-one.vercel.app/?q={query}")
    if response.status_code != 200:
        return await message.reply("➜ erro ao acessar a API do Pinterest")

    images = response.json()
    if not images.get("images"):
        return await message.reply("➜ nenhuma imagem encontrada para a sua pesquisa")

    # Criando um grupo de mídia com as imagens
    media_group = [InputMediaPhoto(media=url) for url in images["images"][:6]]

    msg = await message.reply(f"➜ pesquisando por {query}")
    for count, _ in enumerate(media_group, 1):
        # Atualizando a mensagem com o progresso
        await msg.edit(f"➜ pesquisando por {query} \n➜ {count} de {len(media_group)} imagens encontradas")

    try:
        # Enviando as imagens
        await app.send_media_group(chat_id=message.chat.id, media=media_group, reply_to_message_id=message.id)
    except Exception as e:
        await message.reply(f"➜ erro ao enviar imagens: {e}")
    finally:
        await msg.delete()
