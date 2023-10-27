from pyrogram import filters
from pyrogram.types import Message

from WinxMusic import app
from WinxMusic.misc import SUDOERS
from WinxMusic.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>𝗘𝘅𝗲𝗺𝗽𝗹𝗼 :</b> 📖\n\n/autoend [𝗲𝗻𝗮𝗯𝗹𝗲 | 𝗱𝗶𝘀𝗮𝗯𝗹𝗲] ✅|❌"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "➜ 𝗔𝘂𝘁𝗼 𝗳𝗶𝗻𝗮𝗹𝗶𝘇𝗮çã𝗼 𝗱𝗼 𝘀𝘁𝗿𝗲𝗮𝗺 𝗮𝘁𝗶𝘃𝗮𝗱𝗮. 🔄\n\n𝗢 𝗮𝘀𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗲 𝘀𝗮𝗶𝗿á 𝗮𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗰𝗮𝗺𝗲𝗻𝘁𝗲 𝗱𝗼 𝘃𝗶𝗱𝗲𝗼𝗰𝗵𝗮𝘁 𝗮𝗽ó𝘀 𝗮𝗹𝗴𝘂𝗻𝘀 𝗺𝗶𝗻𝘂𝘁𝗼𝘀 𝘀𝗲 𝗻𝗶𝗻𝗴𝘂é𝗺 𝗲𝘀𝘁𝗶𝘃𝗲𝗿 𝗮𝘀𝘀𝗶𝘀𝘁𝗶𝗻𝗱𝗼. 🎦🕰"
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("➜ 𝗔𝘂𝘁𝗼 𝗲𝗻𝗰𝗲𝗿𝗿𝗮𝗺𝗲𝗻𝘁𝗼 𝗱𝗲 𝘀𝘁𝗿𝗲𝗮𝗺 𝗱𝗲𝘀𝗮𝘁𝗶𝘃𝗮𝗱𝗼 🚫🎥.")
    else:
        await message.reply_text(usage)
