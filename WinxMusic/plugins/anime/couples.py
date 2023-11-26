import random
from datetime import datetime, timedelta
from pyrogram import filters
from WinxMusic import app
from WinxMusic.utils.database import get_couple, save_couple
from config import BANNED_USERS

COUPLE_COMMAND = ["couple", "casal", "winxers"]
PHOTO_URL = "https://telegra.ph/file/908be770f3a34834379f1.png"
COUPLE_SELECTION_MESSAGE = """ <b> 𝗖𝗔𝗦𝗔𝗟 𝗗𝗢 𝗗𝗜𝗔 </b>

{} + {} = ❤️‍🔥

➜ <i> novos casais poderão ser escolhidos amanhã - {} às 12h</i>"""


def get_today_tomorrow():
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    return today.strftime("%d/%m/%Y"), tomorrow.strftime("%d/%m/%Y")


@app.on_message(filters.command(COUPLE_COMMAND) & filters.group & ~BANNED_USERS)
async def couple(_, message):
    chat_id = message.chat.id
    today, tomorrow = get_today_tomorrow()
    is_selected = await get_couple(chat_id, date=today)

    if not is_selected:
        list_of_users = []
        async for member in app.get_chat_members(chat_id, limit=100):
            if not member.user.is_bot:
                list_of_users.append(member.user.id)

        if len(list_of_users) < 2:
            return await message.reply_text("➜ <i> não há membros suficientes para escolher um casal.</i>",
                                            parse_mode="html")

        c1_id, c2_id = random.sample(list_of_users, 2)

        # Obter as menções separadamente
        c1_user = await app.get_users(c1_id)
        c2_user = await app.get_users(c2_id)
        c1_mention = c1_user.mention
        c2_mention = c2_user.mention

        await app.send_photo(chat_id, photo=PHOTO_URL,
                             caption=COUPLE_SELECTION_MESSAGE.format(c1_mention, c2_mention, tomorrow))
        await save_couple(chat_id, today, {"c1_id": c1_id, "c2_id": c2_id})

    else:
        c1_id, c2_id = int(is_selected["c1_id"]), int(is_selected["c2_id"])
        c1_user = await app.get_users(c1_id)
        c2_user = await app.get_users(c2_id)
        c1_mention = c1_user.mention
        c2_mention = c2_user.mention

        await app.send_photo(chat_id, photo=PHOTO_URL,
                             caption=COUPLE_SELECTION_MESSAGE.format(c1_mention, c2_mention, tomorrow))
