import asyncio

from pyrogram import filters
from WinxMusic import app
from WinxMusic.utils.vip_ban import admin_filter

SPAM_CHATS = []


@app.on_message(filters.command(["all", "mention", "mentionall"], prefixes=["/", "@", ".", "#"]) & admin_filter)
async def tag_all_users(_, message):
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text("<i> Me desculpe, migger </i>\n\n"
                                 "<i> Mas você não me deu nada para marcar </i>"
                                 "<i> Use </i> <code>/all [texto]</code> <i> para marcar todos os membros</i>")
        return
    if replied:
        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 5
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 1:
                await replied.reply_text(usertxt)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]

        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 5:
                await message.reply_text(f'{text}\n{usertxt}\n\n|| ➥ desmarcar membros » /cancel ||')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


@app.on_message(
    filters.command(["stopmention", "cancel", "stopall", "cancelmention", "mentionoff", "cancelall", "allcancel"],
                    prefixes=["/", "@", "#"]) & admin_filter)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("<i> marcanção de membros parada com sucesso! </i>")

    else:
        await message.reply_text("<i> Não há marcanção de membros em andamento </i>")
        return
