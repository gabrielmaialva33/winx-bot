import aiohttp
import replicate
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from WinxMusic import app
from WinxMusic.helpers.misc import get_file, get_text
from WinxMusic.misc import AUTHORIZED_CHATS


@app.on_message(
    filters.command(["videofy", "animate"], prefixes=["!", "/"])
    & filters.group
    & ~BANNED_USERS
    & AUTHORIZED_CHATS
)
async def animate(_client, message: Message):
    file = await get_file(message)
    prompt = await get_text(message)

    frames_per_second = int(prompt.split(" ")[0])
    motion_bucket_id = int(prompt.split(" ")[1])

    if file is None:
        return await message.reply_text(
            "💬 responda a uma mensagem com uma 🖼️ para animar ⬆️"
            "ex: !videofy 10 127 (10 frames por segundo e motion bucket id 127)"
        )

    if frames_per_second < 5 or frames_per_second > 30:
        return await message.reply_text(
            "💬 frames por segundo deve estar entre 5 e 30 ⬆️"
        )

    if motion_bucket_id < 1 or motion_bucket_id > 255:
        return await message.reply_text(
            "💬 motion bucket id deve estar entre 1 e 255 ⬆️"
        )

    if frames_per_second is None:
        frames_per_second = 6
    if motion_bucket_id is None:
        motion_bucket_id = 127

    msg = await message.reply_text("<code>⏳animando... 💭</code>")
    try:
        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438",
            input={
                "cond_aug": 0.02,
                "decoding_t": 7,
                "input_image": open(file, "rb"),
                "video_length": "25_frames_with_svd_xt",
                "sizing_strategy": "maintain_aspect_ratio",
                "motion_bucket_id": motion_bucket_id,
                "frames_per_second": frames_per_second,
            },
        )
        if output is None:
            return await msg.edit("❌ erro ao animar imagem 😕")

        await message.reply_video(
            output,
            caption=f"<code>➜ 🖼️ imagem animada </code>",
        )
        await msg.delete()
    except Exception as e:
        await msg.edit(f"➜ ❌ erro ao 🔍 animar 😕: {e}")


@app.on_message(
    filters.command(["music"], prefixes=["!", "/"])
    & filters.group
    & ~BANNED_USERS
    & AUTHORIZED_CHATS
)
async def riffusion(_client, message: Message):
    prompt_a, prompt_b = extract_prompt_ab(message)
    if prompt_a is None or prompt_b is None:
        return await message.reply_text(
            "💬 ➜ envie um texto 🎵 para 🔍 gerar uma música 🎶 se possível em inglês ⬆️ "
            "ex: !music funky synth solo - 90's rap"
        )

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
                "num_inference_steps": 50,
            },
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
        return await message.reply_text(
            "💬 ➜ envie um texto 🎵 para 🔍 gerar uma música 🎶 se possível em inglês ⬆️ "
            "ex: !musicgen funky synth solo 90's rap"
        )

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
            "classifier_free_guidance": 3,
        },
    )
    if output is None:
        return await msg.edit("➜ ❌ erro ao gerar música 😕")

    audio = await aiohttp.ClientSession().get(output)
    audio = await audio.read()
    with open("./cache/musicgen_sound.wav", "wb") as f:
        f.write(audio)
    audio_path = "./cache/musicgen_sound.wav"

    await message.reply_audio(
        audio=audio_path,
        caption=f"<code>➜ 🎵 música gerada com sucesso ⬆️</code>",
    )

    await msg.delete()
