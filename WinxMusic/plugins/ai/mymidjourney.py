import asyncio

import aiohttp
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BANNED_USERS, MIDJOURNEY_KEY
from WinxMusic import LOGGER, app
from WinxMusic.helpers.misc import get_text
from WinxMusic.misc import AUTHORIZED_CHATS

API_URL = "https://api.mymidjourney.ai/api/v1/midjourney"
API_TIMEOUT = 120
HEADERS = {"Accept": "application/json", "Authorization": f"Bearer {MIDJOURNEY_KEY}"}
MSG_PROMPT_MISSING = "🚨Você não me deu um prompt para gerar imagem!"
MSG_PROMPT_NOT_ALLOWED = "⚠️Não foi você quem enviou o prompt"
MSG_ERROR = "⚠️Algo deu errado, tente novamente mais tarde."
# MSG_GENERATING = "🔍"
MSG_GENERATING = "<code>🎨 desenhando... 🎨</code>"
CAPTION = "<b>🎨 Gerado por:</b> <a href='https://t.me/@clubdaswinxcanall'>Winx</a> (<b>Beta</b>)"

prompt_db = {}


@app.on_message(
    filters.command(["mid", "mymidjourney"], prefixes=["!", "/"])
    & filters.group
    & ~BANNED_USERS
    & AUTHORIZED_CHATS
)
async def generate_image(_client, message: Message):
    prompt = await get_text(message)
    if prompt is None:
        return await message.reply_text(MSG_PROMPT_MISSING)

    user = message.from_user
    prompt_data = {
        "prompt": prompt,
        "reply_to_id": message.id,
        "md_id": None,
        "md_original_id": None,
        "user_id": user.id,
    }
    prompt_db[user.id] = prompt_data

    message_id = await create_task_process(message, prompt_data)
    if message_id is None:
        return await message.reply_text(MSG_ERROR)

    await process_image_generation(message, message_id, prompt_data)


async def create_task_process(message: Message, prompt_data):
    LOGGER(__name__).info(
        f"creating task process for {message.from_user.id} with prompt: {prompt_data['prompt']}"
    )
    try:
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=API_TIMEOUT), headers=HEADERS
        ) as session:
            response = await session.post(
                f"{API_URL}/imagine/", data={"prompt": prompt_data["prompt"]}
            )
            data = await response.json()
            if not data.get("success"):
                await message.edit_text(MSG_ERROR)
                return None

            prompt_data["md_id"] = data.get("messageId", None)
            prompt_data["md_original_id"] = data.get("originalMessageId", None)
            prompt_db[message.from_user.id] = prompt_data

            return data.get("messageId", None)
    except Exception as e:
        LOGGER(__name__).error(str(e))
        return None


async def get_task_process(message: Message, mj_id: str):
    LOGGER(__name__).info(
        f"getting task process for {message.from_user.id} with message_id: {mj_id}"
    )
    try:
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=API_TIMEOUT), headers=HEADERS
        ) as session:
            response = await session.get(f"{API_URL}/message/{mj_id}")
            data = await response.json()
            return data
    except Exception as e:
        LOGGER(__name__).error(str(e))
        return None


async def process_image_generation(message: Message, mj_id: str, prompt_data):
    generating = await message.reply_text(MSG_GENERATING)
    while True:
        task_process = await get_task_process(message, mj_id)
        LOGGER(__name__).info(f"task_process: {task_process.get('progress', 0)}")

        if task_process and task_process.get("progress", 0):
            print(task_process["progress"], "%")
            await generating.edit_text(
                f"<code>🎨 desenhando... progresso: {task_process['progress']}%</code>"
            )

        if task_process and task_process.get("progress", 0) == 100:
            break
        if task_process and task_process.get("error"):
            break

        await asyncio.sleep(20)

    if task_process is None:
        await message.reply_text(MSG_ERROR)
        return

    if task_process.get("error"):
        await message.reply_text(MSG_ERROR)
        return

    image_url = task_process["uri"]
    buttons = task_process.get("buttons", [])

    await download_and_send_image(
        message, image_url, buttons, prompt_data["user_id"], prompt_data["reply_to_id"]
    )

    await generating.delete()


async def download_and_send_image(
    message: Message, image_url: str, buttons: list, user_id: int, reply_to_id: int
):
    async with aiohttp.ClientSession() as session:
        response = await session.get(image_url)
        image_data = await response.read()

    image_path = f"cache/{reply_to_id}.png"
    with open(image_path, "wb") as f:
        f.write(image_data)

    await message.reply_photo(
        photo=image_path,
        reply_to_message_id=reply_to_id,
        reply_markup=buttons_markup(buttons, user_id),
        caption=f"{CAPTION}\n\n<b>🔗➜ Link da imagem:</b> <a href='{image_url}'>Clique aqui</a>",
    )


async def task_action(message: Message, mj_id, action):
    LOGGER(__name__).info(
        f"task action for {message.from_user.id} with message_id: {mj_id} and action: {action}"
    )
    async with aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(total=API_TIMEOUT), headers=HEADERS
    ) as session:
        response = await session.post(
            f"{API_URL}/button/", data={"messageId": mj_id, "button": action}
        )
        data = await response.json()
        return data


def buttons_markup(buttons: list, user_id: int):
    all_buttons = [
        [
            InlineKeyboardButton("U1", callback_data=f"U1_{user_id}"),
            InlineKeyboardButton("U2", callback_data=f"U2_{user_id}"),
            InlineKeyboardButton("U3", callback_data=f"U3_{user_id}"),
            InlineKeyboardButton("U4", callback_data=f"U4_{user_id}"),
        ],
        [
            InlineKeyboardButton("🔄", callback_data=f"🔄_{user_id}"),
        ],
        [
            InlineKeyboardButton("V1", callback_data=f"V1_{user_id}"),
            InlineKeyboardButton("V2", callback_data=f"V2_{user_id}"),
            InlineKeyboardButton("V3", callback_data=f"V3_{user_id}"),
            InlineKeyboardButton("V4", callback_data=f"V4_{user_id}"),
        ],
        [
            InlineKeyboardButton(
                "Upscale (2x)", callback_data=f"Upscale (2x)_{user_id}"
            ),
            InlineKeyboardButton(
                "Upscale (4x)", callback_data=f"Upscale (4x)_{user_id}"
            ),
        ],
        [
            InlineKeyboardButton("Zoom Out 2x", callback_data=f"Zoom Out 2x_{user_id}"),
            InlineKeyboardButton(
                "Zoom Out 1.5x", callback_data=f"Zoom Out 1.5x_{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                "Vary (Strong)", callback_data=f"Vary (Strong)_{user_id}"
            ),
            InlineKeyboardButton(
                "Vary (Subtle)", callback_data=f"Vary (Subtle)_{user_id}"
            ),
        ],
        [
            InlineKeyboardButton("⬅️", callback_data=f"⬅️_{user_id}"),
            InlineKeyboardButton("➡️", callback_data=f"➡️_{user_id}"),
            InlineKeyboardButton("⬆️", callback_data=f"⬆️_{user_id}"),
            InlineKeyboardButton("⬇️", callback_data=f"⬇️_{user_id}"),
        ],
    ]

    filtered_buttons = []
    for row in all_buttons:
        new_row = []
        for button in row:
            if button.text in buttons:
                new_row.append(button)
        if new_row:
            filtered_buttons.append(new_row)

    return InlineKeyboardMarkup(filtered_buttons)


@app.on_callback_query(
    filters.regex(
        r"^(U1|U2|U3|U4|V1|V2|V3|V4|Upscale \(2x\)|Upscale \(4x\)|Zoom Out 2x|Zoom Out 1.5x|Vary \(Strong\)|Vary \("
        r"Subtle\)|⬅️|➡️|⬆️|⬇️|🔄)_(\d+)$"
    )
)
async def callback_query_handler(_, callback_query):
    data = callback_query.data.split("_")
    action = data[0]
    user_id = int(data[1])

    if callback_query.from_user.id != user_id:
        return await callback_query.answer(MSG_PROMPT_NOT_ALLOWED, show_alert=True)

    mj_id = prompt_db[user_id]["md_id"]
    await callback_query.answer()

    task = await task_action(callback_query.message, mj_id, action)
    if task and task["success"]:
        await callback_query.message.delete()
        new_mj_id = task["messageId"]
        prompt_db[user_id]["md_id"] = new_mj_id
        await process_image_generation(
            callback_query.message, new_mj_id, prompt_db[user_id]
        )
    else:
        await callback_query.message.edit_text(MSG_ERROR)
