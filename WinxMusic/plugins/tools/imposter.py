from pyrogram import filters
from pyrogram.types import Message

from WinxMusic import app
from WinxMusic.utils import (
    add_userdata,
    check_imposter,
    get_userdata,
    impo_off,
    impo_on,
    usr_data,
)


@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=1)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_imposter(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(
        message.from_user.id
    )
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
🔹 𝗜𝗠𝗣𝗢𝗦𝗧𝗢𝗥 𝗗𝗘𝗧𝗘𝗖𝗧𝗔𝗗𝗢 👀:
➖➖➖➖➖➖➖➖➖➖➖➖
▪️User: {message.from_user.mention}
▪️ID: {message.from_user.id}
➖➖➖➖➖➖➖➖➖➖➖➖\n
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "NO USERNAME"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
🔹𝗠𝗨𝗗𝗢𝗨 𝗢 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘:
➖➖➖➖➖➖➖➖➖➖➖➖
▪️DE: {bef}
▪️PARA: {aft}
➖➖➖➖➖➖➖➖➖➖➖➖\n
""".format(
            bef=usernamebefore, aft=usernameafter
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
🔹𝗠𝗨𝗗𝗢𝗨 𝗢 𝗡𝗢𝗠𝗘:
➖➖➖➖➖➖➖➖➖➖➖➖
▪️DE: {bef}
▪️PARA: {aft}
➖➖➖➖➖➖➖➖➖➖➖➖\n
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "SEM SOBRENOME"
        lastname_after = message.from_user.last_name or "SEM SOBRENOME"
        msg += """
🔹𝗠𝗨𝗗𝗢𝗨 𝗢 𝗦𝗢𝗕𝗥𝗘𝗡𝗢𝗠𝗘:
➖➖➖➖➖➖➖➖➖➖➖➖
▪️DE: {bef}
▪️PARA: {aft}
➖➖➖➖➖➖➖➖➖➖➖➖\n
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo(
            "https://graph.org//file/a5f944533dcaccfaf2567.jpg", caption=msg
        )


@app.on_message(
    filters.group
    & filters.command(["imposter", "impostor"])
    & ~filters.bot
    & ~filters.via_bot
)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("Peça ajuda para saber como usar")
    if message.command[1] == "on":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("➜ Modo Impostor já está ativado")
        else:
            await impo_on(message.chat.id)
            await message.reply(
                f"➜ Modo Impostor ativado com sucesso para {message.chat.title}"
            )
    elif message.command[1] == "off":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("➜ Modo Impostor já está desativado")
        else:
            await impo_off(message.chat.id)
            await message.reply(
                f"➜ Modo Impostor desativado com sucesso para {message.chat.title}"
            )
    else:
        await message.reply("Peça ajuda para saber como usar")
