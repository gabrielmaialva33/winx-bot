from SafoneAPI import SafoneAPI
from pyrogram import *

from WinxMusic import LOGGER, app

api = SafoneAPI()


@app.on_message(filters.command(["ai"], ["!", "/"]))
async def gpt3(_, message):
    if len(message.command) < 2:
        return message.reply_text(
            "<b>Por favor, insira um texto para gerar uma resposta.</b>"
            "\n\n<b>Exemplo:</b> <code>/gpt3 Olá, como você está?</code>"
        )

    input_text = message.text.split(None, 1)[1]
    reply_message = await message.reply_text("<b>🔎 Gerando resposta...</b>")

    try:
        response = await api.chatgpt(input_text, chat_mode="assistant", version=4)
        await reply_message.edit(
            f"<b>🤖 Resposta:</b> <i>{response.choices[0].message.content}</i>"
            f"\n\n<b>ℹ️ Tokens:</b> <code>{response.usage.total_tokens}</code>"
            f"\n<b>🔎 Tokens de conclusão:</b> <code>{response.usage.completion_tokens}</code>"
            f"\n<b>📝 Tokens de prompt:</b> <code>{response.usage.prompt_tokens}</code>"
        )
    except Exception as e:
        LOGGER(__name__).error(e)
        await reply_message.edit("🚫 Algo deu errado!")


@app.on_message(filters.command(["ai4"], ["!", "/"]))
async def gpt3(_, message):
    if len(message.command) < 2:
        return message.reply_text(
            "<b>Por favor, insira um texto para gerar uma resposta.</b>"
            "\n\n<b>Exemplo:</b> <code>/gpt4 Olá, como você está?</code>"
        )

    input_text = message.text.split(None, 1)[1]
    reply_message = await message.reply_text("<b>🔎 Gerando resposta...</b>")

    try:
        response = await api.chatgpt(input_text, chat_mode="assistant", version=4)
        await reply_message.edit(
            f"<b>🤖 Resposta:</b> <i>{response.choices[0].message.content}</i>"
            f"\n\n<b>ℹ️ Tokens:</b> <code>{response.usage.total_tokens}</code>"
            f"\n<b>🔎 Tokens de conclusão:</b> <code>{response.usage.completion_tokens}</code>"
            f"\n<b>📝 Tokens de prompt:</b> <code>{response.usage.prompt_tokens}</code>"
        )
    except Exception as e:
        LOGGER(__name__).error(e)
        await reply_message.edit("🚫 Algo deu errado!")
