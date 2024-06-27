from urllib.parse import urlsplit

import httpx

from .lexica_pastebins import nekobin


async def evaluate_content(text):
    if len(text) < 4096:
        return text
    link = await nekobin(text)
    link += "\n\n#ERROR"
    return link


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
        if (
            message.reply_to_message.document
            and message.reply_to_message.document.file_size > 5242880
        ):
            return 1
        image = await message.reply_to_message.download()
        return image
    else:
        return None


def get_text(message):
    """Extract Text From Commands"""
    text_to_return = message.caption if message.caption else message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


def get_media(message):
    """Extract Media"""
    media = (
        message.media
        if message.media
        else message.reply_to_message.media if message.reply_to_message else None
    )
    if message.media:
        if message.photo:
            media = message.photo
        elif (
            message.document
            and message.document.mime_type in ["image/png", "image/jpg", "image/jpeg"]
            and message.document.file_size < 5242880
        ):
            media = message.document
        else:
            media = None
    elif message.reply_to_message and message.reply_to_message.media:
        if message.reply_to_message.photo:
            media = message.reply_to_message.photo
        elif (
            message.reply_to_message.document
            and message.reply_to_message.document.mime_type
            in ["image/png", "image/jpg", "image/jpeg"]
            and message.reply_to_message.document.file_size < 5242880
        ):
            media = message.reply_to_message.document
        else:
            media = None
    else:
        media = None
    return media


def clean_url(url):
    new_url = urlsplit(url)
    return f"{new_url.scheme}://{new_url.netloc}{new_url.path}"


def get_image_content(url):
    """Get Image Content"""
    try:
        client = httpx.Client()
        response = client.get(clean_url(url))
        if response.status_code != 200:
            return None
        imageType = response.headers["content-type"].split("/")[1]
        if imageType == "gif":
            return None
        return response.content
    except (TimeoutError, httpx.ReadTimeout, httpx.ReadError):
        return None


def get_content_type(url):
    """Get Media Content Type"""
    try:
        client = httpx.Client()
        response = client.head(url)
        if response.status_code != 200:
            return None
        return response.headers["content-type"].split("/")[0]
    except (TimeoutError, httpx.ReadTimeout, httpx.ReadError):
        return None
