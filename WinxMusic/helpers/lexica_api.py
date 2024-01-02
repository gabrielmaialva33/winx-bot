import asyncio

from lexica import AsyncClient

from WinxMusic import LOGGER
from WinxMusic.helpers.misc import ImageModels


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
