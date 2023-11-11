from config import SUPPORT_CHAT
from strings import get_string
from WinxMusic import app
from WinxMusic.misc import SUDOERS
from WinxMusic.utils.database import get_lang, is_maintenance


def language(mystic):
    async def wrapper(_, message, **kwargs):
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} 𝗲𝘀𝘁á 𝗲𝗺 𝗺𝗮𝗻𝘂𝘁𝗲𝗻çã𝗼 🛠️, 𝘃𝗶𝘀𝗶𝘁𝗲 <a href={SUPPORT_CHAT}>𝗰𝗵𝗮𝘁 𝗱𝗲 𝘀𝘂𝗽𝗼𝗿𝘁𝗲</a> 𝗽𝗮𝗿𝗮 𝘀𝗮𝗯𝗲𝗿 𝗼 𝗺𝗼𝘁𝗶𝘃𝗼 🤔.",
                    disable_web_page_preview=True,
                )
        try:
            await message.delete()
        except:
            pass

        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("pt")
        return await mystic(_, message, language)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    f"{app.mention} 𝗲𝘀𝘁á 𝗲𝗺 𝗺𝗮𝗻𝘂𝘁𝗲𝗻çã𝗼 🛠️, 𝘃𝗶𝘀𝗶𝘁𝗲 <a href={SUPPORT_CHAT}>𝗰𝗵𝗮𝘁 𝗱𝗲 𝘀𝘂𝗽𝗼𝗿𝘁𝗲</a> 𝗽𝗮𝗿𝗮 𝘀𝗮𝗯𝗲𝗿 𝗼 𝗺𝗼𝘁𝗶𝘃𝗼 🤔.",
                    show_alert=True,
                )
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            language = get_string(language)
        except:
            language = get_string("pt")
        return await mystic(_, CallbackQuery, language)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("pt")
        return await mystic(_, message, language)

    return wrapper
