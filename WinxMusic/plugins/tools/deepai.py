import requests
from pyrogram import filters
from pyrogram.enums import ChatAction

from WinxMusic import app

api_key = "64102a85-4dbd-4d42-af48-16fe1f31f452"


# api_key = "995e3267-53f1-496e-82e3-39754eab99dc"


@app.on_message(
    filters.command(
        [
            "deep",
        ],
        prefixes=["+", ".", "/", "-", "?", "$", "#", "&"],
    )
)
async def deepchat(app: app, message):
    name = message.from_user.first_name
    try:
        await app.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
                f"Olá {name}\nPor favor, forneça o texto após o comando /deep."
            )
        else:
            a = message.text.split(" ", 1)[1]

            data = {
                "text": a,
            }

            headers = {
                "api-key": api_key,
            }

            r = requests.post(
                "https://api.deepai.org/api/text-generator", data=data, headers=headers
            )
            response = r.json()
            answer_text = response["output"]
            await message.reply_text(f"{answer_text}")
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e}")


#####


@app.on_message(
    filters.command(
        [
            "aby",
        ],
        prefixes=["b", "B"],
    )
)
async def deepchat(app: app, message):
    name = message.from_user.first_name
    try:
        await app.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
                f"Hello {name}\nPlease provide text after the /deep command."
            )
        else:
            a = message.text.split(" ", 1)[1]

            data = {
                "text": a,
            }

            headers = {
                "api-key": api_key,
            }

            r = requests.post(
                "https://api.deepai.org/api/text-generator", data=data, headers=headers
            )
            response = r.json()
            answer_text = response["output"]
            await message.reply_text(f"{answer_text}")
    except Exception as e:
        await message.reply_text(f"ᴇʀʀᴏʀ: {e}")

##
