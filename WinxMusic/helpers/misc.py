async def getFile(message):
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


async def getText(message):
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


ImageModels = {
    "Meina Mix": 2,
    "AnyLora": 3,
    "AnyThing V4": 4,
    "Bing": 6,
    "DarkSushi": 7,
    "Meina Hentai": 8,
    "DarkSushi Mix": 9,
    "Cetus Mix": 10,
    "Creative": 11,
    "Creative V2": 12,
    "Absolute Reality": 13,
    "Concept Art": 15,
    "Lexica": 16,
    "CounterFeitXL": 17,
}
