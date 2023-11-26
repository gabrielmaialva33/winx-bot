from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from youtubesearchpython.__future__ import VideosSearch

from config import BANNED_USERS
from WinxMusic import app
from WinxMusic.utils.inlinequery import answer


@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await client.answer_inline_query(query.id, results=answer, cache_time=10)
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[0]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} 𝗺𝗶𝗻𝘂𝘁𝗼𝘀 | {channel}  | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝗬𝗼𝘂𝘁𝘂𝗯𝗲 🎬",
                            url=link,
                        )
                    ],
                ]
            )
            searched_text = f"""
❄ <b>𝗧𝗶́𝘁𝘂𝗹𝗼:</b> <a href={link}>{title}</a>

⏳ <b>𝗗𝘂𝗿𝗮𝗰̧𝗮̃𝗼:</b> {duration} 𝗺𝗶𝗻𝘂𝘁𝗼𝘀
👀 <b>𝗩𝗶𝘀𝘂𝗮𝗹𝗶𝘇𝗮çõ𝗲𝘀:</b> <code>{views}</code>
🎥 <b>𝗖𝗮𝗻𝗮𝗹:</b> <a href={channellink}>{channel}</a>
⏰ <b>𝗣𝘂𝗯𝗹𝗶𝗰𝗮𝗱𝗼 𝗲𝗺:</b> {published}

<u><b>➜ 𝗠𝗼𝗱𝗼 𝗱𝗲 𝗕𝘂𝘀𝗰𝗮 𝗲𝗺 𝗟𝗶𝗻𝗵𝗮 𝗽𝗼𝗿 {app.name}</b></u>
"""
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await client.answer_inline_query(query.id, results=answers)
        except:
            return
