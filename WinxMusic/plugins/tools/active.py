from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from WinxMusic import app
from WinxMusic.misc import SUDOERS
from WinxMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(filters.command(["activevc", "activevoice"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("➜ 𝗢𝗯𝘁𝗲𝗻𝗱𝗼 𝗹𝗶𝘀𝘁𝗮 𝗱𝗲 𝗰𝗵𝗮𝘁𝘀 𝗱𝗲 𝘃𝗼𝘇 𝗮𝘁𝗶𝘃𝗼𝘀... 🎤🔄")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"➜ 🚫 𝗡ã𝗼 𝗵á 𝗰𝗵𝗮𝘁𝘀 𝗱𝗲 𝘃𝗼𝘇 𝗮𝘁𝗶𝘃𝗼𝘀 𝗲𝗺 {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>➜ 𝗟𝗶𝘀𝘁𝗮 𝗱𝗲 𝗰𝗵𝗮𝘁𝘀 𝗱𝗲 𝘃𝗼𝘇 𝗮𝘁𝗶𝘃𝗼𝘀 𝗮𝘁𝘂𝗮𝗹𝗺𝗲𝗻𝘁𝗲:</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["activev", "activevideo"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("➜ 🔄 𝗕𝘂𝘀𝗰𝗮𝗻𝗱𝗼 𝗹𝗶𝘀𝘁𝗮 𝗱𝗲 𝗰𝗵𝗮𝘁𝘀 𝗱𝗲 𝘃𝗶́𝗱𝗲𝗼 𝗮𝘁𝗶𝘃𝗼𝘀...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"➜ 🚫 𝗡ã𝗼 𝗵á 𝗰𝗵𝗮𝘁𝘀 𝗱𝗲 𝘃𝗶́𝗱𝗲𝗼 𝗮𝘁𝗶𝘃𝗼𝘀 𝗲𝗺 {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>➜ 𝗟𝗶𝘀𝘁𝗮 𝗱𝗲 𝗰𝗵𝗮𝘁𝘀 𝗱𝗲 𝘃𝗶́𝗱𝗲𝗼 𝗮𝘁𝗶𝘃𝗼𝘀 𝗮𝘁𝘂𝗮𝗹𝗺𝗲𝗻𝘁𝗲:</b>\n\n{text}",
            disable_web_page_preview=True,
        )
