import os

from gradio_client import Client
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import Message

import config
from WinxMusic import LOGGER, app
from WinxMusic.misc import AUTHORIZED_CHATS


@app.on_message(
    filters.command(["rvc", "lule"], prefixes=["!", "/"])
    & filters.group
    & ~config.BANNED_USERS
    & AUTHORIZED_CHATS
)
async def inference(bot, message: Message):
    LOGGER(__name__).info(f"{message.from_user.mention} requested to inference audio.")

    client = Client("https://juuxn-simplervc.hf.space/--replicas/h4jl4/")

    try:
        # get a reply audio
        reply = message.reply_to_message
        if not reply.voice:
            await message.reply_text("𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !rvc [audio]")
        else:
            # if audio more 10s not inference
            if reply.voice.duration > 25:
                return await message.reply_text(
                    "𝗔𝘂𝗱𝗶𝗼 𝗺𝘂𝗶𝘁𝗼 𝗹𝗼𝗻𝗴𝗼. 𝗠𝗮𝘅𝗶𝗺𝗼 𝟮𝟱 𝘀𝗲𝗴𝘂𝗻𝗱𝗼𝘀."
                )

            # delete the old audio
            if os.path.exists(f"./downloads/{reply.voice.file_unique_id}.ogg"):
                os.remove(f"./downloads/{reply.voice.file_unique_id}.ogg")

            # download the audio
            await bot.download_media(
                message=reply.voice,
                file_name=f"./downloads/{reply.voice.file_unique_id}.ogg",
            )

            # get the audio file path
            audio_path = f"./downloads/{reply.voice.file_unique_id}.ogg"

            # inference the audio
            result = client.predict(
                "https://huggingface.co/juuxn/RVCModels/resolve/main/Lula.zip",
                "harvest",
                audio_path,
                0,  # Search feature ratio
                -12,  # Número de semitones, subir una octave: 12, bajar una octave: -12
                0,  # Protejer las consonantes sordas y los sonidos respiratorios. 0.5 para desactivarlo.
                0,  # Re-muestreo sobre el audio de salida hasta la frecuencia de muestreo final.
                0,  #  Filtro (reducción de asperezas respiración)
                fn_index=0,
            )

            # get file path
            file_path = result[1]
            if os.path.exists(file_path):
                # send the audio
                await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_AUDIO)

                return await message.reply_audio(
                    audio=file_path, title="Lule 🌈", caption="𝗔𝘂𝗱𝗶𝗼 𝗲𝗱𝗶𝘁𝗮𝗱𝗼 𝗽𝗼𝗿 Winx 🌈"
                )
            else:
                return await message.reply_text("nao deu certo 😥")

    except Exception as e:
        await message.reply_text(f"**𝗘𝗿𝗿𝗼𝗿**: {e} ")