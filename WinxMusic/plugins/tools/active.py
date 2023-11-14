from pyrogram import filters
from pyrogram.types import Message

from WinxMusic import LOGGER, app
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
            chat = await app.get_chat(x)
            if chat.username is not None:
                user = chat.username
                count = chat.members_count
                is_scam = chat.is_scam
                is_fake = chat.is_fake
                invite = await app.export_chat_invite_link(chat.id)

                linked_chat_text = ""
                linked_chat_count = ""
                if chat.linked_chat:
                    linked_chat = await app.get_chat(chat.linked_chat.id)
                    linked_count = linked_chat.members_count
                    linked_chat_text = f"<b>🔗 𝗟𝗶𝗻𝗸𝗲𝗱:</b> <a href=https://t.me/{linked_chat.username}>{linked_chat.username}</a>\n"
                    linked_chat_count = (
                        f"<b>👥 𝗟𝗶𝗻𝗸𝗲𝗱 𝗠𝗲𝗺𝗯𝗿𝗼𝘀:</b> <code>{linked_count}</code>\n"
                    )

                text += (
                    f"<b>{j + 1} ➜ </b> <a href=https://t.me/{user}>{title}</a> [<code>{x}</code>]\n"
                    f"<b>👥 𝗠𝗲𝗺𝗯𝗿𝗼𝘀:</b> <code>{count}</code>\n"
                    f"<b>🚫 𝗘𝘀𝗰𝗮𝗺𝗼𝘀𝗼:</b> {is_scam}\n"
                    f"<b>🚫 𝗙𝗮𝗸𝗲:</b> {is_fake}\n"
                    f"{linked_chat_text}"
                    f"{linked_chat_count}"
                    f"<b>🔗 𝗜𝗻𝘃𝗶𝘁𝗲:</b> {invite}\n\n"
                )
            else:
                count = chat.members_count
                is_scam = chat.is_scam
                is_fake = chat.is_fake
                invite = await app.export_chat_invite_link(chat.id)

                linked_chat_text = ""
                linked_chat_count = ""
                if chat.linked_chat:
                    linked_chat = await app.get_chat(chat.linked_chat.id)
                    linked_chat_text = f"<b>🔗 𝗟𝗶𝗻𝗸𝗲𝗱:</b> <a href=https://t.me/{linked_chat.username}>{linked_chat.username}</a>\n"
                    linked_count = linked_chat.members_count
                    linked_chat_count = (
                        f"<b>👥 𝗟𝗶𝗻𝗸𝗲𝗱 𝗠𝗲𝗺𝗯𝗿𝗼𝘀:</b> <code>{linked_count}</code>\n"
                    )

                text += (
                    f"<b>{j + 1} ➜ </b> {title} [<code>{x}</code>]\n"
                    f"<b>👥 𝗠𝗲𝗺𝗯𝗿𝗼𝘀:</b> <code>{count}</code>\n"
                    f"<b>🚫 𝗘𝘀𝗰𝗮𝗺𝗼𝘀𝗼:</b> {is_scam}\n"
                    f"<b>🚫 𝗙𝗮𝗸𝗲:</b> {is_fake}\n"
                    f"{linked_chat_text}"
                    f"{linked_chat_count}"
                    f"<b>🔗 𝗜𝗻𝘃𝗶𝘁𝗲:</b> {invite}\n\n"
                )
            j += 1
        except Exception as e:
            LOGGER(__name__).error(e)
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
            chat = await app.get_chat(x)
            if chat.username:
                user = chat.username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{title}</a> [<code>{x}</code>]\n"
            else:
                text += f"<b>{j + 1}.</b> {title} [<code>{x}</code>]\n"
            j += 1
        except Exception as e:
            LOGGER(__name__).error(e)
            continue
    if not text:
        await mystic.edit_text(f"➜ 🚫 𝗡ã𝗼 𝗵á 𝗰𝗵𝗮𝘁𝘀 𝗱𝗲 𝘃𝗶́𝗱𝗲𝗼 𝗮𝘁𝗶𝘃𝗼𝘀 𝗲𝗺 {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>➜ 𝗟𝗶𝘀𝘁𝗮 𝗱𝗲 𝗰𝗵𝗮𝘁𝘀 𝗱𝗲 𝘃𝗶́𝗱𝗲𝗼 𝗮𝘁𝗶𝘃𝗼𝘀 𝗮𝘁𝘂𝗮𝗹𝗺𝗲𝗻𝘁𝗲:</b>\n\n{text}",
            disable_web_page_preview=True,
        )
