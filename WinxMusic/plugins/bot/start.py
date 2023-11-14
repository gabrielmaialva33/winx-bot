import time

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from config import BANNED_USERS
from strings import get_string
from WinxMusic import app
from WinxMusic.misc import _boot_
from WinxMusic.plugins.sudo.sudoers import sudoers_list
from WinxMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from WinxMusic.utils.decorators.language import LanguageStart
from WinxMusic.utils.formatters import get_readable_time
from WinxMusic.utils.inline import help_pannel, private_panel, start_panel


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_photo(
                photo=config.START_IMG_URL,
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} 𝗮𝗰𝗮𝗯𝗼𝘂 𝗱𝗲 𝗶𝗻𝗶𝗰𝗶𝗮𝗿 𝗼 𝗯𝗼𝘁 𝗽𝗮𝗿𝗮 "
                    f"𝘃𝗲𝗿𝗶𝗳𝗶𝗰𝗮𝗿 𝗮 <b>𝗹𝗶𝘀𝘁𝗮 𝗱𝗲 𝘀𝘂𝗱𝗼𝘀</b>🔍.\n\n<b>𝗜𝗗 𝗱𝗼 "
                    f"𝘂𝘀𝘂á𝗿𝗶𝗼:</b> <code>{message.from_user.id}</code>🆔\n<b>𝗨𝘀𝘂á𝗿𝗶𝗼:</b> @"
                    f"{message.from_user.username}👤",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} 𝗮𝗰𝗮𝗯𝗼𝘂 𝗱𝗲 𝗶𝗻𝗶𝗰𝗶𝗮𝗿 𝗼 𝗯𝗼𝘁 𝗽𝗮𝗿𝗮 "
                    f"𝘃𝗲𝗿𝗶𝗳𝗶𝗰𝗮𝗿 <b>𝗶𝗻𝗳𝗼𝗿𝗺𝗮çõ𝗲𝘀 𝗱𝗮 𝗲𝗻𝗰𝗼𝗺𝗲𝗻𝗱𝗮</b> 📦.\n\n<b>𝗜𝗗 𝗱𝗼 "
                    f"𝘂𝘀𝘂á𝗿𝗶𝗼:</b> <code>{message.from_user.id}</code> 🆔\n<b>𝗨𝘀𝘂á𝗿𝗶𝗼:</b> @"
                    f"{message.from_user.username} 📛",
                )
    else:
        out = private_panel(_)
        await message.reply_photo(
            photo=config.START_IMG_URL,
            caption=_["start_2"].format(message.from_user.mention, app.mention),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"𝗢 {message.from_user.mention} 𝗮𝗰𝗮𝗯𝗼𝘂 𝗱𝗲 𝗶𝗻𝗶𝗰𝗶𝗮𝗿 𝗼 𝗯𝗼𝘁. 🚀\n\n<b>𝗜𝗗 𝗱𝗼 "
                f"𝘂𝘀𝘂𝗮́𝗿𝗶𝗼:</b> <code>{message.from_user.id}</code> 🆔\n<b>𝗨𝘀𝘂𝗮́𝗿𝗶𝗼:<"
                f"/b> @{message.from_user.username} 📛",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
