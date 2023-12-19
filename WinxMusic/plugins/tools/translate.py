from gpytranslate import Translator
from pyrogram import filters

from config import BANNED_USERS
from WinxMusic import app

# ------------------------------------------------------------------------------- #

trans = Translator()

# Command
TRANSLATOR_COMMAND = ["translate", "traduzir", "tr"]


# ------------------------------------------------------------------------------- #


@app.on_message(filters.command(TRANSLATOR_COMMAND) & filters.group & ~BANNED_USERS)
async def translate(_, message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("𝗥𝗲𝘀𝗽𝗼𝗻𝗱𝗮 𝗮 𝘂𝗺𝗮 𝗺𝗲𝗻𝘀𝗮𝗴𝗲𝗺 𝗽𝗮𝗿𝗮 𝘁𝗿𝗮𝗱𝘂𝘇𝗶𝗿 🌐")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "pt"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = f"𝗧𝗿𝗮𝗱𝘂𝘇𝗶𝗱𝗼 𝗱𝗲 {source} 🌐 𝗽𝗮𝗿𝗮  {dest}:\n" f"`{translation.text}`"
    await message.reply_text(reply)


# ------------------------------------------------------------------------------- #
