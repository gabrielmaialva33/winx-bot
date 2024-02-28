import traceback

from pyrogram import Client, filters, types as t

from WinxMusic import app
from WinxMusic.helpers.lexica_api import lexica_reverse_image_search
from WinxMusic.helpers.lexica_miscs import get_file
from WinxMusic.helpers.telegraph import upload_to_telegraph, GraphClient
from config import BANNED_USERS


@app.on_message(filters.command(["pp", "reverse", "sauce"]) & filters.group & ~BANNED_USERS)
async def reverse_image_search(_: Client, m: t.Message):
    try:
        reply = await m.reply_text("<code>🔍 Downloading...</code>")
        file = await get_file(m)
        if file is None:
            return await reply.edit("Reply to an image?")
        if file == 1:
            return await reply.edit("File size is large")
        await reply.edit("<code> Uploading to the server...</code>")
        img_url = await upload_to_telegraph(file)
        if img_url is None:
            return await reply.edit("Ran into an error.")
        output = await lexica_reverse_image_search(img_url, "google")
        if output['code'] != 2:
            return await reply.edit("Ran into an error.")
        message = ''
        names = output['content']['bestResults']['names']
        urls = output['content']['bestResults']['urls']
        btn = t.InlineKeyboardMarkup(
            [
                [
                    t.InlineKeyboardButton(text="Image URL", url=urls[-1])
                ]
            ])
        if len(names) > 10:
            message = "\n".join([f"{index + 1}. {name}" for index, name in enumerate(names[:10])])
            html_message = f"<br/>".join([f"{index + 1}. {name}" for index, name in enumerate(names)])
            html_message += "<br/><br/><h3>URLS</h3><br/>"
            html_message += f"<br/>".join([f"{url}" for url in urls])
            html_message += "<br/><br/>By <a href='https://t.me/POLWinxBot'>Ｗｉｎｘ Ｂｏｔ</a>"
            url = GraphClient.create_page("More Results", html_message)
            message += f"\n\n<a href='{url}'>More Results</a>\nBy @POLWinxBot"
            await reply.delete()
            return await m.reply_text(message, reply_markup=btn)
        message = "\n".join(
            [f"{index + 1}. {name}" for index, name in enumerate(output['content']['bestResults']['names'])])
        await reply.delete()
        await m.reply_text(f"{message}\n\nBy @POLWinxBot", reply_markup=btn)
    except Exception as E:
        traceback.print_exc()
        return await m.reply_text("Ran into an error.")
