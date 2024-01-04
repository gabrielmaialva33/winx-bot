import aiohttp


async def get_file(message):
    if not message.reply_to_message:
        return None
    if (
            message.reply_to_message.document is False
            or message.reply_to_message.photo is False
    ):
        return None
    if (
            message.reply_to_message.document
            and message.reply_to_message.document.mime_type
            in ["image/png", "image/jpg", "image/jpeg"]
            or message.reply_to_message.photo
    ):
        image = await message.reply_to_message.download()
        return image
    else:
        return None


async def get_text(message):
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


async def telegra_upload(file):
    async with aiohttp.ClientSession() as session:
        binary_file = open(file, "rb")
        data = {"file": binary_file}
        async with session.post("https://telegra.ph/upload", data=data) as resp:
            if resp.status == 200:
                return await resp.json()
            else:
                return None


ImageModels = {
    "Meina Mix|SD": 2,
    "AnyLora|SD": 3,
    "AnyThingV4|SD": 4,
    "Bing|Dall-E": 6,
    "Goofball Mix|SD": 7,
    "MeinaHentai|SD": 8,
    "DarkSushi Mix|SD": 9,
    "SDXL|SDXL 1.0": 10,
    "Creative|SD": 11,
    "CreativeV2|SD": 12,
    "Absolute Reality|SD": 13,
    "CalicoMix|SD": 17,
    "Concept Art|SD": 15,
    "Lexica|SD (Exclusive)": 16,
}

ChatModels = {
    "PaLM": 1,
    "GPT": 5,
    "GPT (Premium)": 19,
    "Llama 2|8B": 18,
    "Llama 2|16B": 14,
    "Bard|LLM": 20,
    "Mistral|LLM": 21,
    "PaLM 2": 23,
}
