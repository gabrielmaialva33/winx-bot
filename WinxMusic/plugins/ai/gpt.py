import asyncio

import aiohttp
from pyrogram import filters

from config import BANNED_USERS
from WinxMusic import app

# --------------------------------------------------------------------------------- #

API_URL = "https://api.qewertyy.me/models"
API_TIMEOUT = 30


# --------------------------------------------------------------------------------- #


async def get_gpt_response(session, api_params):
    async with session.post(API_URL, params=api_params) as response:
        if response.status == 200:
            data = await response.json()
            return data.get("content", "error: api retornou um valor nulo")
        else:
            return f"error: api retornou {response.status} status code"


@app.on_message(filters.command(["gpt", "gpt3"], prefixes=["/", "!"]) & ~BANNED_USERS)
async def gpt3(_client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.reply("por favor, forneça um texto para gerar uma resposta.")
        return

    input_text = args[1]

    try:
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=API_TIMEOUT)
        ) as session:
            result_msg = await message.reply("...")

            api_params = {"model_id": 5, "prompt": input_text}
            api_response = await asyncio.gather(get_gpt_response(session, api_params))

            await result_msg.delete()

    except aiohttp.ClientError as e:
        api_response = f"error: uma exceção ocorreu ao chamar a API.\n\n{e}"
    except asyncio.TimeoutError:
        api_response = "error: api winx timeout."

    reply = message.reply_to_message
    if reply:
        await reply.reply(api_response[0])
    else:
        await message.reply(api_response[0])


@app.on_message(filters.command(["gpt4"], prefixes=["/", "!"]) & ~BANNED_USERS)
async def gpt4(_client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.reply("por favor, forneça um texto para gerar uma resposta.")
        return

    input_text = args[1]

    try:
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=API_TIMEOUT)
        ) as session:
            result_msg = await message.reply("...")

            api_params = {"model_id": 19, "prompt": input_text}
            api_response = await asyncio.gather(get_gpt_response(session, api_params))

            await result_msg.delete()

    except aiohttp.ClientError as e:
        api_response = f"error: uma exceção ocorreu ao chamar a API.\n\n{e}"
    except asyncio.TimeoutError:
        api_response = "error: api winx timeout."

    reply = message.reply_to_message
    if reply:
        await reply.reply(api_response[0])
    else:
        await message.reply(api_response[0])
