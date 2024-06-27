import asyncio
import os
import time
from datetime import datetime, timedelta
from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Voice

import config
from WinxMusic import app
from WinxMusic.utils.formatters import (
    check_duration,
    convert_bytes,
    get_readable_time,
    seconds_to_min,
)


class TeleAPI:
    def __init__(self):
        self.chars_limit = 4096
        self.sleep = 5

    async def send_split_text(self, message, string):
        n = self.chars_limit
        out = [(string[i : i + n]) for i in range(0, len(string), n)]
        j = 0
        for x in out:
            if j <= 2:
                j += 1
                await message.reply_text(x, disable_web_page_preview=True)
        return True

    async def get_link(self, message):
        return message.link

    async def get_filename(self, file, audio: Union[bool, str] = None):
        try:
            file_name = file.file_name
            if file_name is None:
                file_name = "𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗔𝘂𝗱𝗶𝗼 🎵" if audio else "𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗩𝗶́𝗱𝗲𝗼 🎥"
        except:
            file_name = "𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗔𝘂𝗱𝗶𝗼 🎵" if audio else "𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗩𝗶́𝗱𝗲𝗼 🎥"
        return file_name

    async def get_duration(self, file):
        try:
            dur = seconds_to_min(file.duration)
        except:
            dur = "Unknown"
        return dur

    async def get_duration(self, filex, file_path):
        try:
            dur = seconds_to_min(filex.duration)
        except:
            try:
                dur = await asyncio.get_event_loop().run_in_executor(
                    None, check_duration, file_path
                )
                dur = seconds_to_min(dur)
            except:
                return "Unknown"
        return dur

    async def get_filepath(
        self,
        audio: Union[bool, str] = None,
        video: Union[bool, str] = None,
    ):
        if audio:
            try:
                file_name = (
                    audio.file_unique_id
                    + "."
                    + (
                        (audio.file_name.split(".")[-1])
                        if (not isinstance(audio, Voice))
                        else "ogg"
                    )
                )
            except:
                file_name = audio.file_unique_id + "." + "ogg"
            file_name = os.path.join(os.path.realpath("downloads"), file_name)
        if video:
            try:
                file_name = (
                    video.file_unique_id + "." + (video.file_name.split(".")[-1])
                )
            except:
                file_name = video.file_unique_id + "." + "mp4"
            file_name = os.path.join(os.path.realpath("downloads"), file_name)
        return file_name

    async def download(self, _, message, mystic, fname):
        lower = [0, 8, 17, 38, 64, 77, 96]
        higher = [5, 10, 20, 40, 66, 80, 99]
        checker = [5, 10, 20, 40, 66, 80, 99]
        speed_counter = {}
        left_time = {}
        if os.path.exists(fname):
            return True

        async def down_load():
            async def progress(current, total):
                if current == total:
                    return
                current_time = time.time()
                start_time = speed_counter.get(message.id)
                check_time = current_time - start_time
                upl = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="𝗖𝗮𝗻𝗰𝗲𝗹𝗮𝗿 ❌",
                                callback_data="stop_downloading",
                            ),
                        ]
                    ]
                )
                if datetime.now() > left_time.get(message.id):
                    percentage = current * 100 / total
                    percentage = str(round(percentage, 2))
                    speed = current / check_time
                    eta = int((total - current) / speed)
                    eta = get_readable_time(eta)
                    if not eta:
                        eta = "𝟬 𝘀𝗲𝗴𝘂𝗻𝗱𝗼𝘀 ⏲️"
                    total_size = convert_bytes(total)
                    completed_size = convert_bytes(current)
                    speed = convert_bytes(speed)
                    percentage = int((percentage.split("."))[0])
                    text = f"""
➜ 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗦𝘁𝗮𝘁𝘂𝘀:

‣ 𝗧𝗼𝘁𝗮𝗹 𝗦𝗶𝘇𝗲: {total_size}
‣ 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗱: {completed_size}
‣ 𝗣𝗲𝗿𝗰𝗲𝗻𝘁𝗮𝗴𝗲: {percentage}%
‣ 𝗦𝗽𝗲𝗲𝗱: {speed}/s
‣ 𝗘𝗧𝗔: {eta}
"""

                    try:
                        await mystic.edit_text(text, reply_markup=upl)
                    except:
                        pass
                    left_time[message.id] = datetime.now() + timedelta(
                        seconds=self.sleep
                    )

                    for counter in range(7):
                        low = int(lower[counter])
                        high = int(higher[counter])
                        check = int(checker[counter])
                        if low < percentage <= high:
                            if high == check:
                                try:
                                    await mystic.edit_text(
                                        text=_["tg_1"].format(
                                            app.mention,
                                            total_size,
                                            completed_size,
                                            percentage[:5],
                                            speed,
                                            eta,
                                        ),
                                        reply_markup=upl,
                                    )
                                    checker[counter] = 100
                                except:
                                    pass

            speed_counter[message.id] = time.time()
            left_time[message.id] = datetime.now()
            try:
                await app.download_media(
                    message.reply_to_message,
                    file_name=fname,
                    progress=progress,
                )
                try:
                    elapsed = get_readable_time(
                        int(int(time.time()) - int(speed_counter[message.id]))
                    )
                except:
                    elapsed = "𝟬 𝘀𝗲𝗴𝘂𝗻𝗱𝗼𝘀 ⏲️"
                await mystic.edit_text(_["tg_2"].format(elapsed))
            except:
                await mystic.edit_text(_["tg_3"])

        task = asyncio.create_task(down_load())
        config.lyrical[mystic.id] = task
        await task
        verify = config.lyrical.get(mystic.id)
        if not verify:
            return False
        config.lyrical.pop(mystic.id)
        return True
