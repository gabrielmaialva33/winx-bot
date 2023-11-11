import asyncio
import datetime
import logging
import time

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)

from config import OWNER_ID, adminlist
from WinxMusic import app
from WinxMusic.misc import SUDOERS
from WinxMusic.utils.database import (
    get_active_chats,
    get_authuser_names,
    get_client,
    get_served_chats,
    get_served_users,
    remove_served_user,
)
from WinxMusic.utils.decorators.language import language
from WinxMusic.utils.formatters import alpha_to_int

IS_BROADCASTING = False


@app.on_message(filters.command("broadcast") & SUDOERS)
@language
async def broadcast_message(_client, message, _):
    global IS_BROADCASTING
    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(_["broad_2"])
        query = message.text.split(None, 1)[1]
        if "-pin" in query:
            query = query.replace("-pin", "")
        if "-nobot" in query:
            query = query.replace("-nobot", "")
        if "-pinloud" in query:
            query = query.replace("-pinloud", "")
        if "-assistant" in query:
            query = query.replace("-assistant", "")
        if "-user" in query:
            query = query.replace("-user", "")
        if query == "":
            return await message.reply_text(_["broad_8"])

    IS_BROADCASTING = True
    await message.reply_text(_["broad_1"])

    if "-nobot" not in message.text:
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = (
                    await app.forward_messages(i, y, x)
                    if message.reply_to_message
                    else await app.send_message(i, text=query)
                )
                if "-pin" in message.text:
                    try:
                        await m.pin(disable_notification=True)
                        pin += 1
                    except:
                        continue
                elif "-pinloud" in message.text:
                    try:
                        await m.pin(disable_notification=False)
                        pin += 1
                    except:
                        continue
                sent += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                flood_time = int(fw.value)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except:
                continue
        try:
            await message.reply_text(_["broad_3"].format(sent, pin))
        except:
            pass

    if "-user" in message.text:
        susr = 0
        served_users = []
        susers = await get_served_users()
        for user in susers:
            served_users.append(int(user["user_id"]))
        for i in served_users:
            try:
                m = (
                    await app.forward_messages(i, y, x)
                    if message.reply_to_message
                    else await app.send_message(i, text=query)
                )
                susr += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                flood_time = int(fw.value)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except:
                pass
        try:
            await message.reply_text(_["broad_4"].format(susr))
        except:
            pass

    if "-assistant" in message.text:
        aw = await message.reply_text(_["broad_5"])
        text = _["broad_6"]
        from WinxMusic.core.userbot import assistants

        for num in assistants:
            sent = 0
            client = await get_client(num)
            async for dialog in client.get_dialogs():
                try:
                    await client.forward_messages(
                        dialog.chat.id, y, x
                    ) if message.reply_to_message else await client.send_message(
                        dialog.chat.id, text=query
                    )
                    sent += 1
                    await asyncio.sleep(3)
                except FloodWait as fw:
                    flood_time = int(fw.value)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
                except:
                    continue
            text += _["broad_7"].format(num, sent)
        try:
            await aw.edit_text(text)
        except:
            pass
    IS_BROADCASTING = False


async def broadcast_messages(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return True, "Success"
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return await broadcast_messages(user_id, message)
    except InputUserDeactivated:
        await remove_served_user(int(user_id))
        logging.info(f"{user_id} - Removed from database, since deleted account.")
        return False, "Deleted"
    except UserIsBlocked:
        logging.info(f"{user_id} - Blocked the bot.")
        return False, "Blocked"
    except PeerIdInvalid:
        await remove_served_user(int(user_id))
        logging.info(f"{user_id} - PeerIdInvalid")
        return False, "Error"
    except Exception as e:
        return False, "Error"


@app.on_message(filters.command("bc") & filters.user(OWNER_ID) & filters.reply)
async def broadcast_to_all(_bot, message):
    users = await get_served_users()
    b_msg = message.reply_to_message
    status = await message.reply_text(
        text=f"Broadcast em progresso:\n\nTotal de usuários: {len(users)}\n"
    )
    start_time = time.time()
    done = 0
    blocked = 0
    deleted = 0
    failed = 0
    success = 0

    for user in users:
        success, reason = await broadcast_messages(int(user["user_id"]), b_msg)
        if success:
            success += 1
        elif success is False:
            if reason == "Blocked":
                blocked += 1
            elif reason == "Deleted":
                deleted += 1
            elif reason == "Error":
                failed += 1
        done += 1

        if not done % 20:
            await status.edit(
                f"Broadcast in progress:\n\nTotal Users: {len(users)}\nCompleted: {done}/{len(users)}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}"
            )

    time_taken = datetime.timedelta(seconds=int(time.time() - start_time))
    await status.edit(
        f"Broadcast completed:\n\nTotal Users: {len(users)}\nCompleted: {done}/{len(users)}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}\n\nTime taken: {time_taken}"
    )


@app.on_message(filters.command("gc") & filters.user(OWNER_ID) & filters.reply)
async def group_cast(_bot, message):
    chats = await get_served_chats()
    b_msg = message.reply_to_message
    status = await message.reply_text(
        text=f"Broadcast em progresso:\n\nTotal de chats: {len(chats)}\n"
    )
    start_time = time.time()
    done = 0
    failed = 0
    success = 0

    for chat in chats:
        success, reason = await broadcast_messages(int(chat["chat_id"]), b_msg)
        if success:
            success += 1
        elif success is False:
            if reason == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await status.edit(
                f"Broadcast in progress:\n\nTotal Chats: {len(chats)}\nCompleted: {done}/{len(chats)}\nSuccess: {success}\nFailed: {failed}"
            )

    time_taken = datetime.timedelta(seconds=int(time.time() - start_time))
    await status.edit(
        f"Broadcast completed:\n\nTotal Chats: {len(chats)}\nCompleted: {done}/{len(chats)}\nSuccess: {success}\nFailed: {failed}\n\nTime taken: {time_taken}"
    )


async def auto_clean():
    while not await asyncio.sleep(10):
        try:
            served_chats = await get_active_chats()
            for chat_id in served_chats:
                if chat_id not in adminlist:
                    adminlist[chat_id] = []
                    async for user in app.get_chat_members(
                        chat_id, filter=ChatMembersFilter.ADMINISTRATORS
                    ):
                        if user.privileges.can_manage_video_chats:
                            adminlist[chat_id].append(user.user.id)
                    authusers = await get_authuser_names(chat_id)
                    for user in authusers:
                        user_id = await alpha_to_int(user)
                        adminlist[chat_id].append(user_id)
        except:
            continue


asyncio.create_task(auto_clean())
