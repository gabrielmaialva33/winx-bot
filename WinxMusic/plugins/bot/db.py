from pyrogram import Client, filters
from pyrogram.types import Message

from WinxMusic import app, LOGGER
from WinxMusic.utils.database import add_served_chat, get_served_chats


@app.on_message(filters.group & filters.new_chat_members)
async def monitor_chats(_client: Client, message: Message):
    try:
        served_chats = await get_served_chats()
        if message.chat.id not in served_chats:
            await add_served_chat(message.chat.id)
            LOGGER(__name__).info(f"Added {message.chat.id} to served chats list.")
    except Exception as e:
        LOGGER(__name__).warning(e)
