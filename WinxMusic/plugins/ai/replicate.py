import aiohttp
import replicate
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from WinxMusic import LOGGER, app
from WinxMusic.helpers.misc import get_file, get_text
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


@app.on_message(
    filters.command(["music"], prefixes=["!", "/"])
    & filters.group
    & ~BANNED_USERS
    & AUTHORIZED_CHATS
)
async def riffusion(_client, message: Message):
    prompt_a, prompt_b = extract_prompt_ab(message)
    if prompt_a is None or prompt_b is None:
        return await message.reply_text("💬 ➜ envie um texto 🎵 para 🔍 gerar uma música 🎶 se possível em inglês ⬆️ "
                                        "ex: !music funky synth solo - 90's rap")

    msg = await message.reply_text("<code>➜ ⏳gerando música... 💭</code>")

    try:
        output = replicate.run(
            "riffusion/riffusion:8cf61ea6c56afd61d8f5b9ffd14d7c216c0a93844ce2d82ac1c9ecc9c7f24e05",
            input={
                "alpha": 0.5,
                "prompt_a": prompt_a,
                "prompt_b": prompt_b,
                "denoising": 0.75,
                "seed_image_id": "vibes",
                "num_inference_steps": 50
            }
        )
        if output is None:
            return await msg.edit("➜ ❌ erro ao gerar música 😕")

        # save audio in ./cache
        audio = await aiohttp.ClientSession().get(output["audio"])
        audio = await audio.read()
        with open("./cache/gen_sound.wav", "wb") as f:
            f.write(audio)
        audio_path = "./cache/gen_sound.wav"

        await message.reply_audio(
            audio=audio_path,
            caption=f"<code>➜ 🎵 música gerada com sucesso ⬆️</code>",
        )
        await msg.delete()
    except Exception as e:
        await msg.edit(f"➜ ❌ erro ao 🔍 gerar música 😕: {e}")


def extract_prompt_ab(message: Message):
    prompt_a = message.text.split("-")[0].split(" ", 1)[1]
    prompt_b = message.text.split("-")[1].strip()
    return prompt_a, prompt_b


@app.on_message(
    filters.command(["musicgen"], prefixes=["!", "/"])
    & filters.group
    & ~BANNED_USERS
    & AUTHORIZED_CHATS
)
async def musicgen(_, message: Message):
    prompt = await get_text(message)
    if prompt is None:
        return await message.reply_text("💬 ➜ envie um texto 🎵 para 🔍 gerar uma música 🎶 se possível em inglês ⬆️ "
                                        "ex: !musicgen funky synth solo 90's rap")

    msg = await message.reply_text("<code>➜ ⏳gerando música... 💭</code>")
    output = replicate.run(
        "meta/musicgen:b05b1dff1d8c6dc63d14b0cdb42135378dcb87f6373b0d3d341ede46e59e2b38",
        input={
            "top_k": 250,
            "top_p": 0,
            "prompt": prompt,
            "duration": 33,
            "temperature": 1,
            "continuation": False,
            "model_version": "stereo-large",
            "output_format": "wav",
            "continuation_start": 0,
            "multi_band_diffusion": False,
            "normalization_strategy": "peak",
            "classifier_free_guidance": 3
        }
    )
    print(output)
    if output is None:
        return await msg.edit("➜ ❌ erro ao gerar música 😕")

    # save audio in ./cache
    audio = await aiohttp.ClientSession().get(output["audio"])
    audio = await audio.read()
    with open("./cache/musicgen_sound.wav", "wb") as f:
        f.write(audio)
    audio_path = "./cache/musicgen_sound.wav"

    await message.reply_audio(
        audio=audio_path,
        caption=f"<code>➜ 🎵 música gerada com sucesso ⬆️</code>",
    )

    await msg.delete()

