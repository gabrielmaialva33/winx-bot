import os
import random

from openai import OpenAI
from PIL import Image
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import Message

import config
from config import OPEN_AI_API_KEY
from WinxMusic import LOGGER, app
from WinxMusic.misc import AUTHORIZED_CHATS

# Constantes para mensagens e modelos
EXAMPLE_MESSAGE = "𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- {}"
ERROR_MESSAGE = "**𝗘𝗿𝗿𝗼𝗿**: {} "
GPT4_MODEL = "gpt-4"
DALI_MODEL = "dall-e-3"
TTS_MODEL = "tts-1"
VOICES = ["alloy", "echo", "fable", "nova", "onyx", "shimmer"]
DOWNLOADS_PATH = "./downloads/"
TTS_FILE = "tts.ogg"


# Função para limpar arquivos temporários
def clean_temp_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


# Função para baixar e preparar imagem
async def download_and_prepare_image(bot, message, file_name):
    await bot.download_media(message=message, file_name=file_name)
    file = Image.open(file_name)
    file = file.convert("RGBA")
    file.save(file_name)


# Função para processar e enviar resposta
async def process_and_reply(client, bot, message, model, prompt, is_image=False):
    try:
        await bot.send_chat_action(
            message.chat.id,
            ChatAction.TYPING if not is_image else ChatAction.UPLOAD_PHOTO,
        )
        if len(message.command) < 2:
            return await message.reply_text(EXAMPLE_MESSAGE.format(prompt))

        user_input = message.text.split(" ", 1)[1]
        response = None
        if model == GPT4_MODEL:
            response = client.chat.completions.create(
                model=model, messages=[...]
            )  # Adicione a lógica específica aqui
        elif model == DALI_MODEL:
            response = client.images.generate(
                model=model, prompt=user_input, n=1, size="1024x1024"
            )
        # Adicione mais condições conforme necessário

        if is_image:
            image_url = response.data[0].url
            return await message.reply_photo(photo=image_url, caption=user_input)
        else:
            text_response = response.choices[0].message.content
            await message.reply_text(text_response)
    except Exception as e:
        await message.reply_text(ERROR_MESSAGE.format(e))


# Handlers para GPT-4, DALL-E-3, e outros
@app.on_message(
    filters.command(["chatgpt", "gpt4"], prefixes=["!", "/"])
    & filters.group
    & ~config.BANNED_USERS
    & AUTHORIZED_CHATS
)
async def chat(bot, message):
    client = OpenAI(api_key=OPEN_AI_API_KEY)
    await process_and_reply(
        client, bot, message, GPT4_MODEL, "Exemplo: !gpt4 Como consigo uma namorada?"
    )


@app.on_message(
    filters.command(["dalle3", "generation", "gerar"], prefixes=["!", "/"])
    & filters.group
    & ~config.BANNED_USERS
    & AUTHORIZED_CHATS
)
async def generation(bot, message: Message):
    client = OpenAI(api_key=OPEN_AI_API_KEY)
    await process_and_reply(
        client, bot, message, DALI_MODEL, "Exemplo: !gerar uma namorada", is_image=True
    )


@app.on_message(
    filters.command(["variation", "variar"], prefixes=["!", "/"])
    & filters.group
    & ~config.BANNED_USERS
    & AUTHORIZED_CHATS
)
async def variation(bot, message: Message):
    client = OpenAI(api_key=OPEN_AI_API_KEY)
    try:
        # Get the image
        reply = message.reply_to_message
        if not reply.photo:
            return await message.reply_text("𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !variar [imagem]")

        file_path = os.path.join(DOWNLOADS_PATH, "variation.png")
        await download_and_prepare_image(bot, reply, file_path)

        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)

        # Send the image to OpenAI
        with open(file_path, "rb") as img_file:
            response = client.images.create_variation(
                image=img_file, n=1, size="1024x1024"
            )

        # Get the image url and send the image
        image_url = response.data[0].url
        await message.reply_photo(photo=image_url)
    except Exception as e:
        await message.reply_text(ERROR_MESSAGE.format(e))
    finally:
        clean_temp_file(file_path)


@app.on_message(
    filters.command(["edit", "editar"], prefixes=["!", "/"])
    & filters.group
    & ~config.BANNED_USERS
    & AUTHORIZED_CHATS
)
async def edit_image(bot, message: Message):
    client = OpenAI(api_key=OPEN_AI_API_KEY)
    try:
        LOGGER(__name__).info("command: /edit used by %s", message.from_user.first_name)
        # Get the image
        reply = message.reply_to_message
        if not reply.photo or len(message.command) < 2:
            return await message.reply_text(
                "𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !editar [resposta a imagem] + [prompt]"
            )

        prompt = message.text.split(" ", 1)[1]
        file_path = os.path.join(DOWNLOADS_PATH, "edit.png")
        await download_and_prepare_image(bot, reply, file_path)

        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)

        # Send the image to OpenAI
        with open(file_path, "rb") as img_file:
            response = client.images.edit(
                image=img_file, mask=img_file, n=1, size="1024x1024", prompt=prompt
            )

        # Get the image url and send the image
        image_url = response.data[0].url
        await message.reply_photo(photo=image_url, caption=prompt)
    except Exception as e:
        await message.reply_text(ERROR_MESSAGE.format(e))
    finally:
        clean_temp_file(file_path)


@app.on_message(
    filters.command(["tts", "fale"], prefixes=["!", "/"])
    & filters.group
    & ~config.BANNED_USERS
)
async def tts(bot, message: Message):
    client = OpenAI(api_key=OPEN_AI_API_KEY)
    try:
        if len(message.command) < 3:
            return await message.reply_text(
                "𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !tts [voz] [texto]\n𝗩𝗼𝘇𝗲𝘀: " + ", ".join(VOICES)
            )

        voice = message.command[1]
        text = message.command[2]
        voice = voice if voice in VOICES else random.choice(VOICES)

        await bot.send_chat_action(message.chat.id, ChatAction.RECORD_AUDIO)
        response = client.audio.speech.create(model=TTS_MODEL, voice=voice, input=text)

        # Convert to bytes
        audio_data = response.read()

        tts_path = os.path.join(DOWNLOADS_PATH, TTS_FILE)
        with open(tts_path, "wb") as f:
            f.write(audio_data)

        await message.reply_audio(audio=tts_path, caption=f"by voice: {voice}")
    except Exception as e:
        await message.reply_text(ERROR_MESSAGE.format(e))
    finally:
        clean_temp_file(tts_path)
