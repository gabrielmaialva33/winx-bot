import asyncio
import base64
import mimetypes
import os

from lexica import AsyncClient
from lexica.constants import languageModels

from WinxMusic import LOGGER
from WinxMusic.helpers.misc import ImageModels


async def lexica_image_generation(model, prompt):
    try:
        client = AsyncClient()
        output = await client.generate(model, prompt, "")
        if output['code'] != 1:
            return 2
        elif output['code'] == 69:
            return output['code']
        task_id, request_id = output['task_id'], output['request_id']
        await asyncio.sleep(20)
        tries = 0
        image_url = None
        resp = await client.getImages(task_id, request_id)
        while True:
            if resp['code'] == 2:
                image_url = resp['img_urls']
                break
            if tries > 15:
                break
            await asyncio.sleep(5)
            resp = await client.getImages(task_id, request_id)
            tries += 1
            continue
        return image_url
    except Exception as e:
        print(f"Failed to generate the image:", e)
    finally:
        await client.close()


async def lexica_upscale_images(image: bytes) -> str:
    """
    Upscales an image and return with upscaled image path.
    """
    client = AsyncClient()
    content = await client.upscale(image)
    await client.close()
    upscaled_file_path = "upscaled.png"
    with open(upscaled_file_path, "wb") as output_file:
        output_file.write(content)
    return upscaled_file_path


async def lexica_chat_completion(prompt, model) -> tuple | str:
    modelInfo = getattr(languageModels, model)
    client = AsyncClient()
    output = await client.ChatCompletion(prompt, modelInfo)
    await client.close()
    if model == "bard":
        return output['content'], output['images']
    return output['content']


async def lexica_gemini_vision(prompt, model, images) -> tuple | str:
    image_info = []
    for image in images:
        with open(image, "rb") as imageFile:
            data = base64.b64encode(imageFile.read()).decode("utf-8")
            mime_type, _ = mimetypes.guess_type(image)
            image_info.append({
                "data": data,
                "mime_type": mime_type
            })
        os.remove(image)
    payload = {
        "images": image_info
    }
    model_info = getattr(languageModels, model)
    client = AsyncClient()
    output = await client.ChatCompletion(prompt, model_info, json=payload)
    return output['content']['parts'][0]['text']


async def lexica_reverse_image_search(img_url, search_engine) -> dict:
    client = AsyncClient()
    output = await client.ImageReverse(img_url, search_engine)
    await client.close()
    return output


async def lexica_search_images(query, search_engine) -> dict:
    client = AsyncClient()
    output = await client.SearchImages(query, 0, search_engine)
    await client.close()
    return output


async def lexica_download_media(platform, url) -> dict:
    client = AsyncClient()
    output = await client.MediaDownloaders(platform, url)
    await client.close()
    return output


# ------------------------------------------------- #

async def image_generation(model, prompt):
    """
    Generates an image and returns the URL to the image.
    """
    client = AsyncClient()
    try:
        LOGGER(__name__).info(f"Generating image with model {model}")
        if model not in list(ImageModels.values()):
            return 1

        output = await client.generate(model, prompt, "")
        if output["code"] != 1:
            return 2

        task_id, request_id = output["task_id"], output["request_id"]
        await asyncio.sleep(20)

        for _ in range(16):
            resp = await client.getImages(task_id, request_id)
            if resp["code"] == 2:
                return resp["img_urls"]
            await asyncio.sleep(10)
        return None
    except Exception as e:
        LOGGER(__name__).error(f"Failed to generate the image: {e}")
        return None
    finally:
        await client.close()


async def upscale_image(image: bytes) -> str:
    """
    Upscales an image and returns the path to the upscaled image.
    """
    client = AsyncClient()
    try:
        content = await client.upscale(image)
        upscaled_file_path = "upscaled.png"
        with open(upscaled_file_path, "wb") as output_file:
            output_file.write(content)
        return upscaled_file_path
    except Exception as e:
        LOGGER(__name__).error(f"Failed to upscale the image: {e}")
        return ""
    finally:
        await client.close()
