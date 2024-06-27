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
async def animate(_client, message: Message):
    file = await get_file(message)

    if file is None:
        return await message.reply_text(
            "💬 responda a uma mensagem com uma 🖼️ para animar ⬆️" "ex: !videofy"
        )

    msg = await message.reply_text("<code>⏳ animando... 💭</code>")
    try:
        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438",
            input={
                "cond_aug": 0.02,
                "decoding_t": 7,
                "input_image": open(file, "rb"),
                "video_length": "25_frames_with_svd_xt",
                "sizing_strategy": "maintain_aspect_ratio",
                "motion_bucket_id": 127,
                "frames_per_second": 6,
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
    filters.command(["animation"], prefixes=["!", "/"])
    & filters.group
    & ~BANNED_USERS
    & AUTHORIZED_CHATS
)
async def animating(_client, message: Message):
    prompt_a, prompt_b = extract_prompt_ab(message)
    print(prompt_a, prompt_b)
    if prompt_a is None or prompt_b is None:
        return await message.reply_text(
            "💬 ➜ envie uma descrição 🖼️ para animar ⬆️ ela deve conter 2 prompts separados por um traço (-)"
            "ex: !animation tall rectangular black monolith - a rotating black monolith"
        )

    msg = await message.reply_text("<code>⏳ animando... 💭</code>")
    try:
        output = replicate.run(
            "andreasjansson/stable-diffusion-animation:a0cd8005509b772461dd2a4dc58d304bac1d150d93fa35fdc80dc5835f766d4d",
            input={
                "width": 512,
                "height": 512,
                "prompt_end": prompt_a,
                "prompt_start": prompt_b,
                "gif_ping_pong": True,
                "output_format": "mp4",
                "guidance_scale": 7.5,
                "prompt_strength": 0.9,
                "film_interpolation": True,
                "num_inference_steps": 50,
                "num_animation_frames": 25,
                "gif_frames_per_second": 20,
                "num_interpolation_steps": 5,
            },
        )
        if output is None:
            return await msg.edit("❌ erro ao animar imagem 😕")

        await message.reply_video(
            output,
            caption=f"<code>➜ 🖼 animação gerada </code>\n\n➜ prompt: {prompt_a} - {prompt_b}",
        )
        await msg.delete()
    except Exception as e:
        LOGGER(__name__).error(e)
        await msg.edit(f"➜ ❌ erro ao 🔍 animar 😕: {e}")


# @app.on_message(
#     filters.command(["music"], prefixes=["!", "/"])
#     & filters.group
#     & ~BANNED_USERS
#     & AUTHORIZED_CHATS
# )
# async def riffusion(_client, message: Message):
#     prompt_a, prompt_b = extract_prompt_ab(message)
#     if prompt_a is None or prompt_b is None:
#         return await message.reply_text(
#             "💬 ➜ envie um texto 🎵 para 🔍 gerar uma música 🎶 se possível em inglês ⬆️ "
#             "ex: !music funky synth solo - 90's rap"
#         )
#
#     msg = await message.reply_text("<code>➜ ⏳gerando música... 💭</code>")
#
#     try:
#         output = replicate.run(
#             "riffusion/riffusion:8cf61ea6c56afd61d8f5b9ffd14d7c216c0a93844ce2d82ac1c9ecc9c7f24e05",
#             input={
#                 "alpha": 0.5,
#                 "prompt_a": prompt_a,
#                 "prompt_b": prompt_b,
#                 "denoising": 0.75,
#                 "seed_image_id": "vibes",
#                 "num_inference_steps": 50,
#             },
#         )
#         if output is None:
#             return await msg.edit("➜ ❌ erro ao gerar música 😕")
#
#         # save audio in ./cache
#         audio = await aiohttp.ClientSession().get(output["audio"])
#         audio = await audio.read()
#         with open("./cache/gen_sound.wav", "wb") as f:
#             f.write(audio)
#         audio_path = "./cache/gen_sound.wav"
#
#         await message.reply_audio(
#             audio=audio_path,
#             caption=f"<code>➜ 🎵 música gerada com sucesso ⬆️</code>",
#         )
#         await msg.delete()
#     except Exception as e:
#         await msg.edit(f"➜ ❌ erro ao 🔍 gerar música 😕: {e}")
#
#
# @app.on_message(
#     filters.command(["musicgen"], prefixes=["!", "/"])
#     & filters.group
#     & ~BANNED_USERS
#     & AUTHORIZED_CHATS
# )
# async def musicgen(_, message: Message):
#     prompt = await get_text(message)
#     if prompt is None:
#         return await message.reply_text(
#             "💬 ➜ envie um texto 🎵 para 🔍 gerar uma música 🎶 se possível em inglês ⬆️ "
#             "ex: !musicgen funky synth solo 90's rap"
#         )
#
#     msg = await message.reply_text("<code>➜ ⏳gerando música... 💭</code>")
#     output = replicate.run(
#         "meta/musicgen:b05b1dff1d8c6dc63d14b0cdb42135378dcb87f6373b0d3d341ede46e59e2b38",
#         input={
#             "top_k": 250,
#             "top_p": 0,
#             "prompt": prompt,
#             "duration": 33,
#             "temperature": 1,
#             "continuation": False,
#             "model_version": "stereo-large",
#             "output_format": "wav",
#             "continuation_start": 0,
#             "multi_band_diffusion": False,
#             "normalization_strategy": "peak",
#             "classifier_free_guidance": 3,
#         },
#     )
#     if output is None:
#         return await msg.edit("➜ ❌ erro ao gerar música 😕")
#
#     audio = await aiohttp.ClientSession().get(output)
#     audio = await audio.read()
#     with open("./cache/musicgen_sound.wav", "wb") as f:
#         f.write(audio)
#     audio_path = "./cache/musicgen_sound.wav"
#
#     await message.reply_audio(
#         audio=audio_path,
#         caption=f"<code>➜ 🎵 música gerada com sucesso ⬆️</code>",
#     )
#
#     await msg.delete()


# ------------------------------------------------------------------------------------
# Utils
# ------------------------------------------------------------------------------------


def extract_prompt_ab(message: Message):
    prompt_a = message.text.split("-")[0].split(" ", 1)[1]
    prompt_b = message.text.split("-")[1].strip()
    return prompt_a, prompt_b
