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


ImageModels = {
    "MeinaMix|Anime": 2,
    "AnyLora|Anime": 3,
    "AnyThing|Anime": 4,
    "Bing|Dall-E": 6,
    "DarkSushi|Anime": 7,
    "Meina|Hentai": 8,
    "DarkSushiMix|Anime": 9,
    "CetusMix|Anime": 10,
    "Creative|General": 11,
    "CreativeV2|General": 12,
    "AbsoluteReality|Character": 13,
    "ConceptArt|LandScape": 15,
    "Lexica|General": 16,
    "CounterFeitXL|Anime": 17,
}
