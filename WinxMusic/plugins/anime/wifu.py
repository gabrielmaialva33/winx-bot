import logging

import requests
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from WinxMusic import app

WIFU_COMMAND = ["wifu", "waifu"]
API_ENDPOINT = "https://waifu.pics/api/sfw/waifu"

# Inicializando uma sessão HTTP para reutilizar a conexão
session = requests.Session()


def get_waifu_image():
    try:
        response = session.get(API_ENDPOINT)
        response.raise_for_status()

        data = response.json()
        return data.get("url")
    except requests.RequestException as e:
        logging.error(f"erro ao buscar imagem waifu: {e}")
        return None


@app.on_message(filters.command(WIFU_COMMAND) & ~BANNED_USERS)
async def wifu(_, message: Message):
    image_url = get_waifu_image()
    if image_url:
        await message.reply_photo(
            image_url, caption=f" ➜ 🖼 waifu de 👤{message.from_user.first_name} ✅"
        )
    else:
        await message.reply("voçe não tem waifu 😔")
