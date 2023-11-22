import os

from openai import OpenAI
from PIL import Image
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import Message

import config
from config import OPEN_AI_API_KEY
from WinxMusic import LOGGER, app
from WinxMusic.misc import AUTHORIZED_CHATS


@app.on_message(
    filters.command(["chatgpt", "gpt4"], prefixes=["!", "/"])
    & filters.group
    & ~config.BANNED_USERS
    & AUTHORIZED_CHATS
)
async def chat(bot, message):
    client = OpenAI(api_key=OPEN_AI_API_KEY)
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
                "𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !gpt4 𝗖𝗼𝗺𝗼 𝗰𝗼𝗻𝘀𝗲𝗴𝘂𝗶𝗿 𝘂𝗺𝗮 𝗻𝗮𝗺𝗼𝗿𝗮𝗱𝗮?"
            )
        else:
            a = message.text.split(" ", 1)[1]
            MODEL = "gpt-4"
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "A seguir, uma conversa entre um usuário e a Winx uma assistente virtual "
                        "que usa a tecnologia GPT-4 para responder perguntas e conversar com "
                        "você.",
                    },
                    {"role": "assistant", "content": "Olá, eu sou a Winx 🌈"},
                    {"role": "user", "content": a},
                ],
            )

            x = response.choices[0].message.content
            await message.reply_text(f"{x}")
    except Exception as e:
        await message.reply_text(f"**𝗘𝗿𝗿𝗼𝗿**: {e} ")


@app.on_message(
    filters.command(["dall-e-3", "dall-e", "generation", "gerar"], prefixes=["!", "/"])
    & filters.group
    & ~config.BANNED_USERS
    & AUTHORIZED_CHATS
)
async def generation(bot, message: Message):
    LOGGER(__name__).info(
        "command: /generation used by %s", message.from_user.first_name
    )

    client = OpenAI(api_key=OPEN_AI_API_KEY)
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text("𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !gerar 𝘂𝗺𝗮 𝗻𝗮𝗺𝗼𝗿𝗮𝗱𝗮")
        else:
            a = message.text.split(" ", 1)[1]
            MODEL = "dall-e-3"
            response = client.images.generate(
                model=MODEL, prompt=a, n=1, size="1024x1024"
            )
            x = response.data[0].url
            return await message.reply_photo(photo=x, caption=f"{a}")
    except Exception as e:
        if "Error code" in str(e):
            LOGGER(__name__).error(e.message)
            return await message.reply_text(
                "Ocorreu um erro. Por favor, tente novamente mais tarde."
            )
        LOGGER(__name__).error(e)
        await message.reply_text(f"**𝗘𝗿𝗿𝗼𝗿**: {e} ")


@app.on_message(
    filters.command(["variation", "variar"], prefixes=["!", "/"])
    & filters.group
    & ~config.BANNED_USERS
    & AUTHORIZED_CHATS
)
async def variation(bot, message: Message):
    LOGGER(__name__).info(
        "command: /variation used by %s", message.from_user.first_name
    )
    client = OpenAI(api_key=OPEN_AI_API_KEY)
    try:
        # Get the image
        reply = message.reply_to_message
        if not reply.photo:
            await message.reply_text("𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !variar [imagem]")
        else:
            if os.path.exists("./downloads/variation.png"):
                os.remove("./downloads/variation.png")

            # Download the image
            await bot.download_media(
                message=reply,
                file_name="./downloads/variation.png",
            )

            await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)

            # Send the image to OpenAI
            MODEL = "dall-e-3"
            response = client.images.create_variation(
                image=open("./downloads/variation.png", "rb"), n=1, size="1024x1024"
            )
            # Get the image url
            x = response.data[0].url
            # Send the image
            await message.reply_photo(photo=x)
    except Exception as e:
        await message.reply_text(f"**𝗘𝗿𝗿𝗼𝗿**: {e} ")


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
        if not reply.photo:
            await message.reply_text(
                "𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !editar [resposta a imagem] + [prompt]"
            )
        else:
            txt = message.text.split(" ", 1)[1]
            if not txt:
                await message.reply_text(
                    "𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !editar [resposta a imagem] + [prompt]"
                )

            if os.path.exists("./downloads/edit.png"):
                os.remove("./downloads/edit.png")

            # Download the image
            await bot.download_media(
                message=reply,
                file_name="./downloads/edit.png",
            )

            # convert to png
            file = Image.open("./downloads/edit.png")
            file = file.convert("RGBA")
            file.save("./downloads/edit.png")

            await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)

            # Send the image to OpenAI
            response = client.images.edit(
                image=open("./downloads/edit.png", "rb"),
                mask=open("./downloads/edit.png", "rb"),
                n=1,
                size="1024x1024",
                prompt=txt,
            )
            # Get the image url
            x = response.data[0].url
            # Send the image
            await message.reply_photo(photo=x, caption=txt)
    except Exception as e:
        await message.reply_text(f"**𝗘𝗿𝗿𝗼𝗿**: {e} ")


@app.on_message(
    filters.command(["tts", "fale"], prefixes=["!", "/"])
    & filters.group
    & ~config.BANNED_USERS
)
async def tts(bot, message: Message):
    client = OpenAI(api_key=OPEN_AI_API_KEY)
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.RECORD_AUDIO)

        if len(message.command) < 2:
            await message.reply_text("𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !tts 𝘂𝗺𝗮 𝗳𝗿𝗮𝘀𝗲")
        else:
            a = message.text.split(" ", 1)[1]
            MODEL = "tts-1"
            VOICE = "nova"
            response = client.audio.speech.create(model=MODEL, voice=VOICE, input=a)

            print(response)
            # <openai._base_client.HttpxBinaryResponseContent object at 0x1218fe610>
            # convert to bytes
            bt = response.read()

            if os.path.exists("./downloads/tts.ogg"):
                os.remove("./downloads/tts.ogg")

            # tts.ogg in ./downloads/tts.ogg
            with open("./downloads/tts.ogg", "wb") as f:
                f.write(bt)
            await message.reply_audio(audio="./downloads/tts.ogg")
    except Exception as e:
        await message.reply_text(f"**𝗘𝗿𝗿𝗼𝗿**: {e} ")
