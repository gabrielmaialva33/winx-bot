import asyncio

from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import PLAYLIST_IMG_URL, QUEUE_LIMIT, SUPPORT_CHAT, adminlist
from strings import get_string
from WinxMusic import YouTube, app
from WinxMusic.misc import SUDOERS, db
from WinxMusic.utils.database import (
    get_assistant,
    get_cmode,
    get_lang,
    get_playmode,
    get_playtype,
    is_active_chat,
    is_maintenance,
)
from WinxMusic.utils.inline import botplaylist_markup

links = {}


def PlayWrapper(command):
    async def wrapper(client, message):
        language = await get_lang(message.chat.id)
        _ = get_string(language)
        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝗖𝗼𝗺𝗼 𝗰𝗼𝗿𝗿𝗶𝗴𝗶𝗿? 🛠️",
                            callback_data="AnonymousAdmin",
                        ),
                    ]
                ]
            )
            return await message.reply_text(_["general_3"], reply_markup=upl)

        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} 𝗲𝘀𝘁á 𝗲𝗺 𝗺𝗮𝗻𝘂𝘁𝗲𝗻çã𝗼, 𝘃𝗶𝘀𝗶𝘁𝗲 <a href={SUPPORT_CHAT}>𝘀𝘂𝗽𝗽𝗼𝗿𝘁 𝗰𝗵𝗮𝘁</a> 𝗽𝗮𝗿𝗮 𝘀𝗮𝗯𝗲𝗿 𝗮 𝗿𝗮𝘇ã𝗼.",
                    disable_web_page_preview=True,
                )
        if await is_active_chat(message.chat.id):
            check = db.get(message.chat.id)

            if len(check) > QUEUE_LIMIT:
                return await message.reply_text(
                    text=f"𝗣𝗮𝗿𝗲𝗰𝗲 𝗾𝘂𝗲 𝘃𝗼𝗰ê 𝗲𝘀𝘁á 𝗲𝘀𝘁á 𝗳𝗮𝘇𝗲𝗻𝗱𝗼 𝗷𝗮𝗳á 10 𝗺ú𝘀𝗶𝗰𝗮𝘀 𝗻𝗮 𝗳𝗶𝗹𝗮. 𝗣𝗼𝗿 𝗳𝗮𝘃𝗼𝗿, 𝗮𝗴𝘂𝗮𝗿𝗱𝗲 𝗮 𝗳𝗶𝗻𝗮𝗹𝗶𝘇𝗮𝗿 𝗽𝗮𝗿𝗮 𝘁𝗲𝗿𝗺𝗶𝗻𝗮𝗿 𝗲𝘀𝘁𝗮 𝘂𝘁𝗶𝗹𝗶𝘇𝗮𝗿 𝗲𝗹𝗮𝘀 𝘂𝘁𝗶𝗹𝗶𝘇𝗮𝗿 /𝗲𝗻𝗱. 🕒",
                    disable_web_page_preview=True,
                )
        try:
            await message.delete()
        except:
            pass

        audio_telegram = (
            (message.reply_to_message.audio or message.reply_to_message.voice)
            if message.reply_to_message
            else None
        )
        video_telegram = (
            (message.reply_to_message.video or message.reply_to_message.document)
            if message.reply_to_message
            else None
        )
        url = await YouTube.url(message)
        if audio_telegram is None and video_telegram is None and url is None:
            if len(message.command) < 2:
                if "stream" in message.command:
                    return await message.reply_text(_["str_1"])
                buttons = botplaylist_markup(_)
                return await message.reply_photo(
                    photo=PLAYLIST_IMG_URL,
                    caption=_["play_18"],
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
        if message.command[0][0] == "c":
            chat_id = await get_cmode(message.chat.id)
            if chat_id is None:
                return await message.reply_text(_["setting_7"])
            try:
                chat = await app.get_chat(chat_id)
            except:
                return await message.reply_text(_["cplay_4"])
            channel = chat.title
        else:
            chat_id = message.chat.id
            channel = None
        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)
        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_13"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["play_4"])
        if message.command[0][0] == "v":
            video = True
        else:
            if "-v" in message.text:
                video = True
            else:
                video = True if message.command[0][1] == "v" else None
        if message.command[0][-1] == "e":
            if not await is_active_chat(chat_id):
                return await message.reply_text(_["play_16"])
            fplay = True
        else:
            fplay = None

        if not await is_active_chat(chat_id):
            userbot = await get_assistant(chat_id)
            try:
                try:
                    if userbot is None:
                        return await message.reply_text(
                            f"𝗡ã𝗼 𝗳𝗼𝗶 𝗽𝗼𝘀𝘀𝗶́𝘃𝗲𝗹 𝗲𝗻𝗰𝗼𝗻𝘁𝗿𝗮𝗿 𝗼 𝗮𝘀𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗲 𝗽𝗮𝗿𝗮 "
                            f"𝗲𝘀𝘁𝗲 𝗰𝗵𝗮𝘁! 😕 𝗧𝗲𝗻𝘁𝗲 𝗱𝗮𝗿 𝗮𝗱𝗺𝗶𝗻 𝗽𝗿𝗮 𝗪𝗶𝗻𝘅 👑 𝗲 𝘁𝗲𝗻𝘁𝗲 𝗻𝗼𝘃𝗮𝗺𝗲𝗻𝘁𝗲 🔁"
                        )
                    get = await app.get_chat_member(chat_id, userbot.id)
                except ChatAdminRequired:
                    return await message.reply_text(_["call_1"])
                if (
                    get.status == ChatMemberStatus.BANNED
                    or get.status == ChatMemberStatus.RESTRICTED
                ):
                    return await message.reply_text(
                        _["call_2"].format(
                            app.mention, userbot.id, userbot.name, userbot.username
                        )
                    )
            except UserNotParticipant:
                if chat_id in links:
                    invitelink = links[chat_id]
                else:
                    if message.chat.username:
                        invitelink = message.chat.username
                        try:
                            await userbot.resolve_peer(invitelink)
                        except:
                            pass
                    else:
                        try:
                            invitelink = await app.export_chat_invite_link(chat_id)
                        except ChatAdminRequired:
                            return await message.reply_text(_["call_1"])
                        except Exception as e:
                            return await message.reply_text(
                                _["call_3"].format(app.mention, type(e).__name__)
                            )

                if invitelink.startswith("https://t.me/+"):
                    invitelink = invitelink.replace(
                        "https://t.me/+", "https://t.me/joinchat/"
                    )
                myu = await message.reply_text(_["call_4"].format(app.mention))
                try:
                    await asyncio.sleep(1)
                    await userbot.join_chat(invitelink)
                except InviteRequestSent:
                    try:
                        await app.approve_chat_join_request(chat_id, userbot.id)
                    except Exception as e:
                        return await message.reply_text(
                            _["call_3"].format(app.mention, type(e).__name__)
                        )
                    await asyncio.sleep(3)
                    await myu.edit(_["call_5"].format(app.mention))
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    return await message.reply_text(
                        _["call_3"].format(app.mention, type(e).__name__)
                    )

                links[chat_id] = invitelink

                try:
                    await userbot.resolve_peer(chat_id)
                except:
                    pass

        return await command(
            client,
            message,
            _,
            chat_id,
            video,
            channel,
            playmode,
            url,
            fplay,
        )

    return wrapper
