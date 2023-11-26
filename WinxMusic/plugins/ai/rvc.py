import os

from gradio_client import Client
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import Message
from unidecode import unidecode

import config
from WinxMusic import LOGGER, app
from WinxMusic.misc import AUTHORIZED_CHATS

# Constantes para mensagens
AUDIO_LONG_MESSAGE = "🎙️ Áudio muito longo 🚫. Máximo ⏱️ 25 segundos ⏳."
REPLY_AUDIO_MESSAGE = "👋 Olá winxer 🤖\n💡 Exemplo: - !{} [responder a um 🎙️ áudio] 💬"
ERROR_MESSAGE = "❌ erro: {} 💬"
INFERRED_AUDIO_CAPTION = "🎙️𝗔𝘂𝗱𝗶𝗼 𝗶𝗻𝗳𝗲𝗿𝗶𝗱𝗼 𝗽𝗼𝗿 {} 🤖"

# Modelo e URL de cada personagem
MODEL_URLS = {
    "lule": "https://huggingface.co/juuxn/RVCModels/resolve/main/Lula.zip",
    "bolso": "https://huggingface.co/juuxn/RVCModels/resolve/main/Bolsonaro.zip",
}


# Função para checar e baixar áudio
def check_and_download_audio(bot, message, max_duration=25):
    if not message.reply_to_message or not message.reply_to_message.voice:
        cmd = message.text.split()[0].lstrip("!/")
        message.reply_text(REPLY_AUDIO_MESSAGE.format(cmd))
        return None

    reply = message.reply_to_message
    if reply.voice.duration > max_duration:
        message.reply_text(AUDIO_LONG_MESSAGE)
        return None

    audio_path = f"./downloads/{reply.voice.file_unique_id}.ogg"
    if os.path.exists(audio_path):
        os.remove(audio_path)

    bot.download_media(message=reply.voice, file_name=audio_path)
    return audio_path


# Função genérica para inferência de áudio
def audio_inference(bot, message, character):
    LOGGER(__name__).info(
        f"requested to {character}fy audio by {message.from_user.first_name}"
    )

    client = Client(
        "https://juuxn-simplervc.hf.space/--replicas/h4jl4/", output_dir="./downloads"
    )
    audio_path = check_and_download_audio(bot, message)
    if audio_path is None:
        return

    try:
        model_url = MODEL_URLS.get(character, "")
        result = client.predict(
            model_url, "rmvpe", audio_path, 0.75, 0, 0.33, 0, 3, fn_index=0
        )

        file_path = result[1]
        if file_path:
            new_name = f"./downloads/{character.capitalize()}_{unidecode(message.from_user.first_name).strip().replace(' ', '_')}.wav"
            os.rename(file_path, new_name)
            bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_AUDIO)
            message.reply_audio(
                audio=new_name,
                caption=INFERRED_AUDIO_CAPTION.format(character.capitalize()),
            )
        else:
            message.reply_text("𝗘𝗿𝗿𝗼𝗿 𝗮𝗼 𝗶𝗻𝗳𝗲𝗿𝗶𝗿 𝗼 𝗮𝘂𝗱𝗶𝗼.")
    except Exception as e:
        message.reply_text(ERROR_MESSAGE.format(e))


# Comandos
@app.on_message(
    filters.command(["lule", "lulify"], prefixes=["!", "/"])
    & filters.group
    & ~config.BANNED_USERS
    & AUTHORIZED_CHATS
)
def lula_inference(bot, message: Message):
    audio_inference(bot, message, "lule")


@app.on_message(
    filters.command(["bolso", "bolsofy"], prefixes=["!", "/"])
    & filters.group
    & ~config.BANNED_USERS
    & AUTHORIZED_CHATS
)
def bolso_inference(bot, message: Message):
    audio_inference(bot, message, "bolso")
