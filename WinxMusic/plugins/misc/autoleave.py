import asyncio
from datetime import datetime

from pyrogram.enums import ChatType

import config
from WinxMusic import app
from WinxMusic.core.call import Winx, autoend
from WinxMusic.utils.database import get_client, is_active_chat, is_autoend


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT is True:
        while not await asyncio.sleep(config.LEAVE_TIME):
            from WinxMusic.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                left = 0
                try:
                    async for i in client.get_dialogs():
                        if i.chat.type in [
                            ChatType.SUPERGROUP,
                            ChatType.GROUP,
                            ChatType.CHANNEL,
                        ]:
                            if (
                                i.chat.id != config.LOGGER_ID
                                and i.chat.id != -1001621792868
                            ):
                                if left == 20:
                                    continue
                                if not await is_active_chat(i.chat.id):
                                    try:
                                        await client.leave_chat(i.chat.id)
                                        left += 1
                                    except:
                                        continue
                except:
                    pass


# asyncio.create_task(auto_leave())


async def auto_end():
    while not await asyncio.sleep(5):
        ender = await is_autoend()
        if not ender:
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await Winx.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "➜ 𝗕𝗼𝘁 𝘀𝗮𝗶𝘂 𝗮𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗰𝗮𝗺𝗲𝗻𝘁𝗲 𝗱𝗼 𝘃𝗶́𝗱𝗲𝗼𝗰𝗵𝗮𝘁 𝗽𝗼𝗶𝘀 𝗻𝗶𝗻𝗴𝘂𝗲́𝗺 𝗲𝘀𝘁𝗮𝘃𝗮 𝗼𝘂𝘃𝗶𝗻𝗱𝗼 🎥🤖💨.",
                    )
                except:
                    continue


asyncio.create_task(auto_end())
