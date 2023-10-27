from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="P𝗮𝘂𝘀𝗮𝗿",
            description=f"𝗣𝗮𝘂𝘀𝗮𝗿 𝗺𝘂́𝘀𝗶𝗰𝗮 𝗻𝗼 𝗩𝗶𝗱𝗲𝗼𝗰𝗵𝗮𝘁.",
            thumb_url="https://telegra.ph/file/3757031c66beb34fd8db9.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="R𝗲𝘀𝘂𝗺𝗶𝗿",
            description=f"𝗥𝗲𝘀𝘂𝗺𝗲 𝗼 𝗽𝗹𝗮𝘆𝗲𝗿 𝗱𝗲 𝗺𝘂́𝘀𝗶𝗰𝗮 𝗻𝗼 𝗩𝗶𝗱𝗲𝗼𝗰𝗵𝗮𝘁.",
            thumb_url="https://telegra.ph/file/3757031c66beb34fd8db9.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="S𝗸𝗶𝗽",
            description=f"S𝗸𝗶𝗽 𝗮 𝗺𝘂́𝘀𝗶𝗰𝗮 𝗮𝗰𝘁𝘂𝗮𝗹 𝗱𝗲 𝗽𝗹𝗮𝘆𝗲𝗿 𝗻𝗼 𝗩𝗶𝗱𝗲𝗼𝗰𝗵𝗮𝘁.",
            thumb_url="https://telegra.ph/file/3757031c66beb34fd8db9.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="F𝗶𝗺",
            description="F𝗶𝗺 𝗮 𝗺𝘂́𝘀𝗶𝗰𝗮 𝗮𝗰𝘁𝘂𝗮𝗹 𝗱𝗲 𝗽𝗹𝗮𝘆𝗲𝗿 𝗻𝗼 𝗩𝗶𝗱𝗲𝗼𝗰𝗵𝗮𝘁.",
            thumb_url="https://telegra.ph/file/3757031c66beb34fd8db9.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="𝗦𝗵𝘂𝗳𝗳𝗹𝗲",
            description="𝗦𝗵𝘂𝗳𝗳𝗹𝗲 𝗮 𝗺𝘂́𝘀𝗶𝗰𝗮 𝗮𝗰𝘁𝘂𝗮𝗹 𝗱𝗲 𝗽𝗹𝗮𝘆𝗲𝗿 𝗻𝗼 𝗩𝗶𝗱𝗲𝗼𝗰𝗵𝗮𝘁.",
            thumb_url="https://telegra.ph/file/3757031c66beb34fd8db9.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="𝗟𝗼𝗼𝗽",
            description="𝗟𝗼𝗼𝗽 𝗮 𝗺𝘂́𝘀𝗶𝗰𝗮 𝗮𝗰𝘁𝘂𝗮𝗹 𝗱𝗲 𝗽𝗹𝗮𝘆𝗲𝗿 𝗻𝗼 𝗩𝗶𝗱𝗲𝗼𝗰𝗵𝗮𝘁.",
            thumb_url="https://telegra.ph/file/3757031c66beb34fd8db9.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
