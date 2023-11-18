from openai import OpenAI
from pyrogram import filters
from pyrogram.enums import ChatAction

from config import OPEN_AI_API_KEY
from WinxMusic import app

client = OpenAI(api_key=OPEN_AI_API_KEY)


@app.on_message(
    filters.command(
        ["chatgpt", "gpt4"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]
    )
)
async def chat(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
                "𝗢𝗹𝗮́ 𝘄𝗶𝗻𝘅𝗲𝗿\n𝗘𝘅𝗲𝗺𝗽𝗹𝗼:- !gpt4 𝗖𝗼𝗺𝗼 𝗰𝗼𝗻𝘀𝗲𝗴𝘂𝗶𝗿 𝘂𝗺𝗮 𝗻𝗮𝗺𝗼𝗿𝗮𝗱𝗮?"
            )
        else:
            a = message.text.split(" ", 1)[1]
            MODEL = "gpt-4"
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {
                        "role": "system",
                        "text": "A seguir, uma conversa entre um usuário e a Winx uma assistente virtual "
                        "que usa a tecnologia GPT-4 para responder perguntas e conversar com você.",
                    },
                    {"role": "user", "content": a},
                ],
                temperature=0.2,
            )
            x = resp["choices"][0]["message"]["content"]
            await message.reply_text(f"{x}")
    except Exception as e:
        await message.reply_text(f"**𝗘𝗿𝗿𝗼𝗿**: {e} ")
