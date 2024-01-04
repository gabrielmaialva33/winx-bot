import aiohttp
import replicate
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from WinxMusic import LOGGER, app
from WinxMusic.helpers.misc import get_file
from WinxMusic.misc import AUTHORIZED_CHATS


@app.on_message(
    filters.command(["videofy", "animate"], prefixes=["!", "/"])
    & filters.group
    & ~BANNED_USERS
    & AUTHORIZED_CHATS
)
async def generate_image(_client, message: Message):
    LOGGER(__name__).info(f" animate command received by {message.from_user.id}")
    file = await get_file(message)
    if file is None:
        return await message.reply_text(
            "💬 ➜ responda a uma mensagem com uma 🖼️ para animar ⬆️"
        )

    msg = await message.reply_text("<code>➜ ⏳animando... 💭</code>")
    try:
        telegra_file = await telegra_upload(file)
        if telegra_file is None:
            return await msg.edit("➜ ❌ erro ao enviar imagem para o telegra.ph 😕")

        file_name = telegra_file[0]["src"].split("/")[-1]
        file_url = f"https://telegra.ph/file/{file_name}"

        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438",
            input={
                "cond_aug": 0.02,
                "decoding_t": 7,
                "input_image": file_url,
                "video_length": "25_frames_with_svd_xt",
                "sizing_strategy": "maintain_aspect_ratio",
                "motion_bucket_id": 127,
                "frames_per_second": 6,
            },
        )
        if output is None:
            return await msg.edit("➜ ❌ erro ao animar imagem 😕")

        await message.reply_video(
            output,
            caption=f"<code>➜ 🖼️ imagem animada com sucesso ⬆️</code>",
        )
        await msg.delete()
    except Exception as e:
        await msg.edit(f"➜ ❌ erro ao 🔍 animar 😕: {e}")


async def telegra_upload(file):
    async with aiohttp.ClientSession() as session:
        binary_file = open(file, "rb")
        data = {"file": binary_file}
        async with session.post("https://telegra.ph/upload", data=data) as resp:
            if resp.status == 200:
                return await resp.json()
            else:
                return None
