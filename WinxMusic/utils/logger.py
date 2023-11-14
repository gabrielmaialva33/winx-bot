from pyrogram.enums import ParseMode

from config import LOGGER_ID
from WinxMusic import app
from WinxMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} 𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝗼 𝗱𝗲 𝗽𝗹𝗮𝘆</b>

<b>𝗜𝗗 𝗱𝗼 𝗰𝗵𝗮𝘁 :</b> <code>{message.chat.id}</code>
<b>𝗡𝗼𝗺𝗲 𝗱𝗼 𝗰𝗵𝗮𝘁 :</b> {message.chat.title}
<b>𝗨𝘀𝘂á𝗿𝗶𝗼 𝗱𝗼 𝗰𝗵𝗮𝘁 :</b> @{message.chat.username}
<b>𝗧𝗶𝗽𝗼 𝗱𝗲 𝗰𝗵𝗮𝘁 :</b> {message.chat.type}
<b>𝗡𝘂𝗺𝗲𝗿𝗼 𝗱𝗲 𝗺𝗲𝗺𝗯𝗿𝗼𝘀 :</b> {await app.get_chat_members_count(message.chat.id)}
<b>🚫 𝗘𝘀𝗰𝗮𝗺𝗼𝘀𝗼:</b> {message.chat.is_scam}
<b>🚫 𝗙𝗮𝗸𝗲:</b> {message.chat.is_fake}
<b>𝗜𝗻𝘃𝗶𝘁𝗲 𝗱𝗲 𝗰𝗵𝗮𝘁 :</b> {await app.export_chat_invite_link(message.chat.id)}

<b>𝗜𝗗 𝗱𝗼 𝘂𝘀𝘂á𝗿𝗶𝗼 :</b> <code>{message.from_user.id}</code>
<b>𝗡𝗼𝗺𝗲 :</b> {message.from_user.mention}
<b>𝗨𝘀𝘂á𝗿𝗶𝗼 :</b> @{message.from_user.username}

<b>𝗤𝘂𝗲𝗿𝘆 :</b> {message.text.split(None, 1)[1]}
<b>𝗧𝗶𝗽𝗼 𝗱𝗲 𝘀𝘁𝗿𝗲𝗮𝗺 :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return


async def restart_logs(message):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} 𝗥𝗲𝗻𝗶𝗰𝗶𝗮𝗱𝗼</b>

<b>𝗜𝗗 𝗱𝗼 𝗰𝗵𝗮𝘁 :</b> <code>{message.chat.id}</code>
<b>𝗡𝗼𝗺𝗲 𝗱𝗼 𝗰𝗵𝗮𝘁 :</b> {message.chat.title}
<b>𝗨𝘀𝘂á𝗿𝗶𝗼 𝗱𝗼 𝗰𝗵𝗮𝘁 :</b> @{message.chat.username}

<b>𝗜𝗗 𝗱𝗼 𝘂𝘀𝘂á𝗿𝗶𝗼 :</b> <code>{message.from_user.id}</code>
<b>𝗡𝗼𝗺𝗲 :</b> {message.from_user.mention}
<b>𝗨𝘀𝘂á𝗿𝗶𝗼 :</b> @{message.from_user.username}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
