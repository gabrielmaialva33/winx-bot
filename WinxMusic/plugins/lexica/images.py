import io
import random
import traceback

from pyrogram import Client, errors, filters
from pyrogram import types as t

from WinxMusic import app
from WinxMusic.helpers.lexica_api import lexica_search_images
from WinxMusic.helpers.lexica_miscs import get_image_content, get_text


@app.on_message(filters.command(["img", "imagesearch"]) & filters.group)
async def search_images(_: Client, m: t.Message):
    try:
        reply = await m.reply_text("<code>🔍 Procurando...</code>")
        prompt = get_text(m)
        if prompt is None:
            return await reply.edit("O que você quer que eu procure?")
        output = await lexica_search_images(prompt, "google")
        if output["code"] != 2:
            return await reply.edit("Ran into an error.")
        images = output["content"]
        if len(images) == 0:
            return await reply.edit("No results found.")
        images = random.choices(images, k=8 if len(images) > 8 else len(images))
        media = []
        for image in images:
            content = get_image_content(image["imageUrl"])
            if content is None:
                images.remove(image)
                continue
            else:
                media.append(t.InputMediaPhoto(io.BytesIO(content)))
        await m.reply_media_group(media, quote=True)
        await reply.delete()
    except (
        errors.ExternalUrlInvalid,
        errors.WebpageCurlFailed,
        errors.WebpageMediaEmpty,
    ) as e:
        print(e)
        return await reply.edit("Ran into an error.")
    except Exception as e:
        traceback.print_exc()
        return await reply.edit("Ran into an error.")
