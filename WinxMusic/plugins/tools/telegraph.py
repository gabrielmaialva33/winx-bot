import base64

import httpx
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegraph import upload_file

from WinxMusic import app


@app.on_message(filters.reply & filters.command(["tgm", "telegraph"]))
async def upscale_image(client, message):
    try:
        if not message.reply_to_message or not message.reply_to_message.photo:
            await message.reply_text(
                "𝐩𝐨𝐫 𝐟𝐚𝐯𝐨𝐫, 𝐫𝐞𝐬𝐩𝐨𝐧𝐝𝐚 𝐚 𝐮𝐦𝐚 𝐢𝐦𝐚𝐠𝐞𝐦 𝐩𝐚𝐫𝐚 𝐜𝐫𝐢𝐚𝐫 𝐬𝐞𝐮 𝐥𝐢𝐧𝐤 𝐧𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡."
            )
            return

        sent_message = await message.reply_text(
            "ᴏᴋ, ᴀɢᴜᴀʀᴅᴇ ᴜᴍ ᴘᴏᴜᴄᴏ ᴄʀɪᴀɴᴅᴏ ᴏ ʟɪɴᴋ ᴅᴏ ᴛᴇʟᴇɢʀᴀᴘʜ ᴅᴀ sᴜᴀ ɪᴍᴀɢᴇᴍ ғᴏʀɴᴇᴄɪᴅᴀ ᴇᴍ ᴀʟᴛᴀ ᴅᴇғɪɴɪçãᴏ..."
        )

        image = message.reply_to_message.photo.file_id
        file_path = await client.download_media(image)

        with open(file_path, "rb") as image_file:
            f = image_file.read()

        b = base64.b64encode(f).decode("utf-8")

        async with httpx.AsyncClient() as http_client:
            response = await http_client.post(
                "https://api.qewertyy.me/upscale", data={"image_data": b}, timeout=None
            )

        with open("upscaled_image.png", "wb") as output_file:
            output_file.write(response.content)

        # Upload the upscaled image to Telegraph
        telegraph_url = upload_file("upscaled_image.png")[0]

        # Create caption with the Telegraph link as a button
        button_text = "๏ ᴀʙʀɪʀ ɴᴏ ᴛᴇʟᴇɢʀᴀᴘʜ ๏"
        button_url = "https://telegra.ph" + telegraph_url
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(button_text, url=button_url)]]
        )

        await client.send_photo(
            message.chat.id,
            photo="upscaled_image.png",
            caption=f"**➲ 𝐀𝐪𝐮𝐢 𝐞𝐬𝐭𝐚́ 𝐨 𝐬𝐞𝐮 𝐥𝐢𝐧𝐤 𝐝𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡 𝐩𝐚𝐫𝐚 𝐚 𝐟𝐨𝐭𝐨 𝐞𝐦 "
            f"𝐇𝐃.**\n\n**๏ 𝐕𝐨𝐜𝐞̂ 𝐩𝐨𝐝𝐞 𝐜𝐨𝐩𝐢𝐚𝐫 𝐜𝐥𝐢𝐜𝐚𝐧𝐝𝐨 𝐚𝐪𝐮𝐢: **\n\n"
            f"**‣**  `{button_url}`\n\n**๏ 𝐏𝐨𝐫 @{app.username}**",
            reply_markup=reply_markup,
        )

        # Delete the "Wait making link.." message after sending the results
        await sent_message.delete()

    except Exception as e:
        print(f"𝐅𝐚𝐥𝐡𝐚 𝐚𝐨 𝐚𝐦𝐩𝐥𝐢𝐚𝐫 𝐚 𝐢𝐦𝐚𝐠𝐞𝐦: {e}")
        await message.reply_text(
            "𝐅𝐚𝐥𝐡𝐚 𝐚𝐨 𝐚𝐦𝐩𝐥𝐢𝐚𝐫 𝐚 𝐢𝐦𝐚𝐠𝐞𝐦. 𝐏𝐨𝐫 𝐟𝐚𝐯𝐨𝐫, 𝐭𝐞𝐧𝐭𝐞 𝐧𝐨𝐯𝐚𝐦𝐞𝐧𝐭𝐞 𝐦𝐚𝐢𝐬 𝐭𝐚𝐫𝐝𝐞"
        )
