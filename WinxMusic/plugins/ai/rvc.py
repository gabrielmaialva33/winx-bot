import os

from gradio_client import Client
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import Message
from unidecode import unidecode

import config
from WinxMusic import LOGGER, app
from WinxMusic.misc import AUTHORIZED_CHATS


@app.on_message(
    filters.command(["rvc", "lule", "lulify"], prefixes=["!", "/"])
    & filters.group
    & ~config.BANNED_USERS
    & AUTHORIZED_CHATS
)
def lula_inference(bot, message: Message):
    LOGGER(__name__).info(
        f"requested to lulify audio by {message.from_user.first_name}"
    )

    client = Client(
        "https://juuxn-simplervc.hf.space/--replicas/h4jl4/", output_dir="./downloads"
    )

    try:
        if not message.reply_to_message:
            message.reply_text("𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !rvc [responder a um audio]")
            return

        reply = message.reply_to_message

        if not reply.voice:
            message.reply_text("𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !rvc [responder a um audio]")
        else:
            # if audio more 10s not inference
            if reply.voice.duration > 25:
                return message.reply_text("𝗔𝘂𝗱𝗶𝗼 𝗺𝘂𝗶𝘁𝗼 𝗹𝗼𝗻𝗴𝗼. 𝗠𝗮𝘅𝗶𝗺𝗼 𝟮𝟱 𝘀𝗲𝗴𝘂𝗻𝗱𝗼𝘀.")

            # delete the old audio
            if os.path.exists(f"./downloads/{reply.voice.file_unique_id}.ogg"):
                os.remove(f"./downloads/{reply.voice.file_unique_id}.ogg")

            # set the audio path
            audio_path = f"./downloads/{reply.voice.file_unique_id}.ogg"

            # download the audio
            bot.download_media(
                message=reply.voice,
                file_name=audio_path,
            )

            # inference the audio
            result = client.predict(
                "https://huggingface.co/juuxn/RVCModels/resolve/main/Lula.zip",
                "harvest",
                audio_path,
                0,  # Search feature ratio
                -12,  # Número de semitones, subir una octave: 12, bajar una octave: -12
                0,  # Protejer las consonantes sordas y los sonidos respiratorios. 0.5 para desactivarlo.
                0,  # Re-muestreo sobre el audio de salida hasta la frecuencia de muestreo final.
                0,  # Filtro (reducción de asperezas respiración)
                fn_index=0,
            )

            # get file path
            file_path = result[1]

            if file_path is not None:
                novo_nome = f"./downloads/Lulify_{unidecode(reply.from_user.first_name).strip().replace(' ', '_')}.wav"
                os.rename(file_path, novo_nome)

                # send the audio
                bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_AUDIO)

                message.reply_audio(
                    audio=novo_nome, caption="𝗔𝘂𝗱𝗶𝗼 𝗶𝗻𝗳𝗲𝗿𝗶𝗱𝗼 𝗽𝗼𝗿 𝗟𝘂𝗹𝗮 🤖"
                )
            else:
                message.reply_text("𝗘𝗿𝗿𝗼𝗿 𝗮𝗼 𝗶𝗻𝗳𝗲𝗿𝗶𝗿 𝗼 𝗮𝘂𝗱𝗶𝗼.")

    except Exception as e:
        message.reply_text(f"**𝗘𝗿𝗿𝗼𝗿**: {e} ")


@app.on_message(
    filters.command(["rvc", "bolso", "bolsofy"], prefixes=["!", "/"])
    & filters.private
    & ~config.BANNED_USERS
    & AUTHORIZED_CHATS
)
def bolso_inference(bot, message: Message):
    LOGGER(__name__).info(
        f"requested to bolsofy audio by {message.from_user.first_name}"
    )

    client = Client(
        "https://juuxn-simplervc.hf.space/--replicas/h4jl4/", output_dir="./downloads"
    )

    try:
        if not message.reply_to_message:
            message.reply_text("𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !rvc [responder a um audio]")
            return

        reply = message.reply_to_message

        if not reply.voice:
            message.reply_text("𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !rvc [responder a um audio]")
        else:
            # if audio more 10s not inference
            if reply.voice.duration > 25:
                return message.reply_text("𝗔𝘂𝗱𝗶𝗼 𝗺𝘂𝗶𝘁𝗼 𝗹𝗼𝗻𝗴𝗼. 𝗠𝗮𝘅𝗶𝗺𝗼 𝟮𝟱 𝘀𝗲𝗴𝘂𝗻𝗱𝗼𝘀.")

            # delete the old audio
            if os.path.exists(f"./downloads/{reply.voice.file_unique_id}.ogg"):
                os.remove(f"./downloads/{reply.voice.file_unique_id}.ogg")

            # set the audio path
            audio_path = f"./downloads/{reply.voice.file_unique_id}.ogg"

            # download the audio
            bot.download_media(
                message=reply.voice,
                file_name=audio_path,
            )

            # inference the audio
            result = client.predict(
                "https://huggingface.co/juuxn/RVCModels/resolve/main/Bolsonaro.zip",
                "harvest",
                audio_path,
                0,  # Search feature ratio
                -12,  # Número de semitones, subir una octave: 12, bajar una octave: -12
                0,  # Protejer las consonantes sordas y los sonidos respiratorios. 0.5 para desactivarlo.
                0,  # Re-muestreo sobre el audio de salida hasta la frecuencia de muestreo final.
                0,  # Filtro (reducción de asperezas respiración)
                fn_index=0,
            )

            # get file path
            file_path = result[1]

            if file_path is not None:
                novo_nome = f"./downloads/Bolsofy_{unidecode(reply.from_user.first_name).strip().replace(' ', '_')}.wav"
                os.rename(file_path, novo_nome)

                print(novo_nome, "novo_nome")
                # send the audio
                bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_AUDIO)

                message.reply_audio(
                    audio=novo_nome, caption="𝗔𝘂𝗱𝗶𝗼 𝗶𝗻𝗳𝗲𝗿𝗶𝗱𝗼 𝗽𝗼𝗿 𝗟𝘂𝗹𝗮 🤖"
                )
            else:
                message.reply_text("𝗘𝗿𝗿𝗼𝗿 𝗮𝗼 𝗶𝗻𝗳𝗲𝗿𝗶𝗿 𝗼 𝗮𝘂𝗱𝗶𝗼.")

    except Exception as e:
        message.reply_text(f"**𝗘𝗿𝗿𝗼𝗿**: {e} ")
