from functools import wraps
import traceback, sys, re

from config import LOGGER_ID
from .lexica_miscs import evaluate_content
from urllib.parse import urlsplit

media_pattern = r"\b(https?://(?:(.*?)\.)?(?:instagram\.com|www\.instagram\.com|t\.co|twitter\.com|x\.com|pin\.it|pinterest\.com|in\.pinterest\.com)(?:[^\s]*))\b"


def error_handler(func):
    @wraps(func)
    async def wrapper(client, message, *args, **kwargs):
        try:
            await func(client, message, *args, **kwargs)
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                exc_type,
                exc_obj,
                exc_tb,
            )
            errors = await evaluate_content(
                "#ERROR | `{}` | `{}`\n\n`{}`\n```{}```\n".format(
                    0 if not message.from_user else message.from_user.id,
                    0 if not message.chat else message.chat.id,
                    message.caption if message.caption else message.text,
                    "".join(errors),
                ),
            )
            await client.send_message(LOGGER_ID, errors)
            raise err

    return wrapper


def identify_platform(func):
    @wraps(func)
    async def wrapper(client, message, *args, **kwargs):
        url = re.findall(media_pattern, message.text)[0][0]
        platform = urlsplit(url).netloc.split('.')[-2]
        message.platform = "pinterest" if platform == "pin" else platform
        message.url = url
        await func(client, message, *args, **kwargs)

    return wrapper
