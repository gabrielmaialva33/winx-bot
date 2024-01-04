import asyncio
import os
import shutil
import socket
from datetime import datetime

import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import filters

import config
from WinxMusic import app
from WinxMusic.misc import HAPP, SUDOERS, XCB
from WinxMusic.utils.database import (
    get_active_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from WinxMusic.utils.decorators.language import language
from WinxMusic.utils.logger import restart_logs
from WinxMusic.utils.pastebin import WinxBin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def is_heroku():
    return "heroku" in socket.getfqdn()


@app.on_message(filters.command(["getlog", "logs", "getlogs"]) & SUDOERS)
@language
async def log_(client, message, _):
    try:
        await message.reply_document(document="log.txt")
    except:
        await message.reply_text(_["server_1"])


@app.on_message(filters.command(["update", "gitpull"]) & SUDOERS)
@language
async def update_(client, message, _):
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(_["server_2"])
    response = await message.reply_text(_["server_3"])
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit(_["server_4"])
    except InvalidGitRepositoryError:
        return await response.edit(_["server_5"])
    to_exc = f"git fetch origin {config.UPSTREAM_BRANCH} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]
    for checks in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit(_["server_6"])
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[(format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4],
    )
    for info in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        updates += f"<b>➣ #{info.count()}: <a href={REPO_}/commit/{info}>{info.summary}</a> ʙʏ -> {info.author}</b>\n\t\t\t\t<b>➥ 𝗖𝗼𝗺𝗽𝗿𝗼𝗺𝗲𝘁𝗶𝗱𝗼 𝗲𝗺 :</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    _update_response_ = "<b>𝗨𝗺𝗮 𝗻𝗼𝘃𝗮 𝗮𝘁𝘂𝗮𝗹𝗶𝘇𝗮çã𝗼 𝗲𝘀𝘁á 𝗱𝗶𝘀𝗽𝗼𝗻𝗶𝘃𝗲𝗹 𝗽𝗮𝗿𝗮 𝗼 𝗯𝗼𝘁!</b>\n\n➣ 𝗔𝗽𝗹𝗶𝗰𝗮𝗻𝗱𝗼 𝗮𝘁𝘂𝗮𝗹𝗶𝘇𝗮çõ𝗲𝘀 𝗮𝗴𝗼𝗿𝗮\n\n<b><u>𝗔𝘁𝘂𝗮𝗹𝗶𝘇𝗮çõ𝗲𝘀:</u></b>\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        url = await WinxBin(updates)
        nrs = await response.edit(
            f"<b>𝗨𝗺𝗮 𝗻𝗼𝘃𝗮 𝗮𝘁𝘂𝗮𝗹𝗶𝘇𝗮çã𝗼 𝗲𝘀𝘁á 𝗱𝗶𝘀𝗽𝗼𝗻𝗶𝘃𝗲𝗹 𝗽𝗮𝗿𝗮 𝗼 𝗯𝗼𝘁!</b>\n\n➣ 𝗔𝗽𝗹𝗶𝗰𝗮𝗻𝗱𝗼 𝗮𝘁𝘂𝗮𝗹𝗶𝘇𝗮çõ𝗲𝘀 𝗮𝗴𝗼𝗿𝗮\n\n<u><b>𝗔𝘁𝘂𝗮𝗹𝗶𝘇𝗮çõ𝗲𝘀:</b></u>\n\n<a href={url}>𝗖𝗼𝗻𝗳𝗲𝗿𝗶𝗿 𝗮𝘁𝘂𝗮𝗹𝗶𝘇𝗮çõ𝗲𝘀</a>"
        )
    else:
        nrs = await response.edit(_final_updates_, disable_web_page_preview=True)
    os.system("git stash &> /dev/null && git pull")

    try:
        served_chats = await get_active_chats()
        for x in served_chats:
            try:
                await app.send_message(
                    chat_id=int(x),
                    text=_["server_8"].format(app.mention),
                )
                await remove_active_chat(x)
                await remove_active_video_chat(x)
            except:
                pass
        await response.edit(f"{nrs.text}\n\n{_['server_7']}")
    except:
        pass

    if await is_heroku():
        try:
            os.system(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0] * 2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            return
        except Exception as err:
            await response.edit(f"{nrs.text}\n\n{_['server_9']}")
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=_["server_10"].format(err),
            )
    else:
        os.system("pip3 install -r requirements.txt")
        os.system(f"kill -9 {os.getpid()} && python3 -m WinxMusic")
        exit()


@app.on_message(filters.command(["restart"]) & SUDOERS)
async def restart_(_, message):
    response = await message.reply_text("𝗿𝗲𝗶𝗻𝗶𝗰𝗶𝗮𝗻𝗱𝗼... 🔄")
    await restart_logs(message)
    ac_chats = await get_active_chats()
    for x in ac_chats:
        try:
            await app.send_message(
                chat_id=int(x),
                text=f"{app.mention} 𝗲𝘀𝘁á 𝗿𝗲𝗶𝗻𝗶𝗰𝗶𝗮𝗻𝗱𝗼... 🔄\n\n𝗩𝗼𝗰ê 𝗽𝗼𝗱𝗲𝗿á 𝘃𝗼𝗹𝘁𝗮𝗿 𝗮 𝘁𝗼𝗰𝗮𝗿 𝗲𝗺 15-20 𝘀𝗲𝗴𝘂𝗻𝗱𝗼𝘀. ⏳",
            )
            await remove_active_chat(x)
            await remove_active_video_chat(x)
        except:
            pass

    try:
        shutil.rmtree("downloads")
        shutil.rmtree("raw_files")
        shutil.rmtree("cache")
    except:
        pass
    await response.edit_text(
        "➜ 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗼 𝗱𝗲 𝗿𝗲𝗶𝗻𝗶𝗰𝗶𝗮𝗿 𝗶𝗻𝗶𝗰𝗶𝗮𝗱𝗼, 𝗽𝗼𝗿 𝗳𝗮𝘃𝗼𝗿 𝗮𝗴𝘂𝗮𝗿𝗱𝗲 𝗮𝗹𝗴𝘂𝗻𝘀 𝘀𝗲𝗴𝘂𝗻𝗱𝗼𝘀 𝗮𝘁é 𝗾𝘂𝗲 𝗼 𝗯𝗼𝘁 𝗰𝗼𝗺𝗲𝗰𝗲..."
    )
    os.system(f"kill -9 {os.getpid()} && python3 -m WinxMusic")
