from pyrogram import filters

from WinxMusic import app


@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"➜ 𝗦𝗲𝘂 𝗜𝗗: {message.from_user.id}\n{reply.from_user.first_name}'𝗦 𝗜𝗗: {reply.from_user.id}\n➜ "
            f"𝗖𝗵𝗮𝘁 𝗜𝗗: {message.chat.id}"
        )
    else:
        message.reply(f"➜ 𝗦𝗲𝘂 𝗜𝗗: {message.from_user.id}\n➜ 𝗖𝗵𝗮𝘁 𝗜𝗗: {message.chat.id}")
