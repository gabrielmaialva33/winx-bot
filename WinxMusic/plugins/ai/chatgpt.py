from openai import OpenAI
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import Message

from config import OPEN_AI_API_KEY
from WinxMusic import app


@app.on_message(filters.command(["chatgpt", "gpt4"], prefixes=["!", "/"]))
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
    filters.command(["dall-e-3", "dall-e", "generation", "img"], prefixes=["!", "/"])
)
async def dall_e(bot, message: Message):
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
            return await message.reply_photo(photo=x)
    except Exception as e:
        if "content_policy_violation" in str(e):
            return await message.reply_text(
                "O seu prompt contém conteúdo inapropriado."
            )
        if "Error code" in str(e):
            return await message.reply_text(
                "Ocorreu um erro. Por favor, tente novamente mais tarde."
            )
        await message.reply_text(f"**𝗘𝗿𝗿𝗼𝗿**: {e} ")
