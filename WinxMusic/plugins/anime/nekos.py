import requests
from pyrogram import filters
from pyrogram.types import Message

from WinxMusic import app

# --------------------------------------------------------------------------------- #

NEKO_CUDDLE_COMMAND = ["cuddle", "carinho"]
NEKO_SHRUG_COMMAND = ["shrug", "encolher os ombros"]
NEKO_POKE_COMMAND = ["poke", "cutucar"]
NEKO_FACEPALM_COMMAND = ["facepalm", "rosto na palma da mão"]
NEKO_STARE_COMMAND = ["stare", "encarar"]
NEKO_POUT_COMMAND = ["pout", "fazer beicinho"]
NEKO_HANDHOLD_COMMAND = ["handhold", "segurar a mão"]
NEKO_WAVE_COMMAND = ["wave", "acenar"]
NEKO_BLUSH_COMMAND = ["blush", "ficar corado"]
NEKO_NEKO_COMMAND = ["neko", "transformar em neko"]
NEKO_DANCE_COMMAND = ["dance", "dançar"]
NEKO_BAKA_COMMAND = ["baka", "chamar de idiota"]
NEKO_BORE_COMMAND = ["bore", "ficar entediado"]
NEKO_LAUGH_COMMAND = ["laugh", "rir"]
NEKO_SMUG_COMMAND = ["smug", "olhar presunçoso"]
NEKO_THUMBSUP_COMMAND = ["thumbsup", "dar polegar para cima"]
NEKO_SHOOT_COMMAND = ["shoot", "atirar"]
NEKO_TICKLE_COMMAND = ["tickle", "fazer cócegas"]
NEKO_FEED_COMMAND = ["feed", "alimentar"]
NEKO_THINK_COMMAND = ["think", "pensar"]
NEKO_WINK_COMMAND = ["wink", "piscar"]
NEKO_SLEEP_COMMAND = ["sleep", "dormir"]
NEKO_PUNCH_COMMAND = ["punch", "soco"]
NEKO_CRY_COMMAND = ["cry", "chorar"]
NEKO_KILL_COMMAND = ["kill", "matar"]
NEKO_SMILE_COMMAND = ["smile", "sorrir"]
NEKO_HIGHFIVE_COMMAND = ["highfive", "dar um toque"]
NEKO_SLAP_COMMAND = ["slap", "dar um tapa"]
NEKO_HUG_COMMAND = ["hug", "abraçar"]
NEKO_PAT_COMMAND = ["pat", "fazer carinho"]
NEKO_WAIFU_COMMAND = ["waifu", "wafu"]


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_CUDDLE_COMMAND))
def cuddle(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/cuddle").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} **𝗖𝗮𝗿𝗶𝗻𝗵𝗼 𝗲𝗺 💖✨** {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/cuddle").json()
        url = api["results"][0]["url"]
        m.reply_animation(
            animation=url, caption=f"{m.from_user.first_name} 𝗙𝗮𝘇 𝗰𝗮𝗿𝗶𝗻𝗵𝗼 😌🤗"
        )


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_SHRUG_COMMAND))
def shrug(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/shrug").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"𝗖𝗲 𝗳𝗼𝗱𝗮 𝗱𝗲 💥🤯 {m.from_user.first_name} 𝗣𝗿𝗮 𝘂 🤷‍♂️📞🚫 {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/shrug").json()
        url = api["results"][0]["url"]
        m.reply_animation(
            animation=url, caption=f"{m.from_user.first_name} **ce foda**"
        )


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_POKE_COMMAND))
def poke(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/poke").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗖𝘂𝘁𝘂𝗰𝗮 🧐 𝘂 {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/poke").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} 𝗖𝘂𝘁𝘂𝗰𝗮 🧐")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_FACEPALM_COMMAND))
def facepalm(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/facepalm").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"😕 {m.from_user.first_name} 𝗻 𝘀𝘂𝗽𝗼𝗿𝘁𝗮 🚫 𝗼 𝗯𝘂𝗿𝗿𝗲 🐴 𝗱𝘂 {reply.from_user.first_name} 🌈",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/facepalm").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} 𝗯𝘂𝗿𝗿𝗲")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_STARE_COMMAND))
def stare(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/stare").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url, caption=f"𝗢𝗹𝗵𝗮𝗻𝗱𝘂 𝗽𝗮𝗿𝗮 👀 {reply.from_user.first_name} 🌈"
        )
    else:
        api = requests.get("https://nekos.best/api/v2/stare").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name}𝗢𝗹𝗵𝗮𝗻𝗱𝘂 👀")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_POUT_COMMAND))
def pout(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/pout").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗕𝗶𝗰𝗼 𝗽𝗮𝗿𝗮 🐦👄 {reply.from_user.first_name}  🌈",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/pout").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name}  𝗕𝗶𝗰𝗼 🐦👄")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_HANDHOLD_COMMAND))
def handhold(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/handhold").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗦𝗲𝗴𝘂𝗿𝗮 𝗮 𝗺ã𝗼 𝗱𝗲 ✋🤝 {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/handhold").json()
        url = api["results"][0]["url"]
        m.reply_animation(
            animation=url, caption=f"{m.from_user.first_name} 𝗦𝗲𝗴𝘂𝗿𝗮 𝗮 𝗺ã𝗼 ✋🤝"
        )


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_WAVE_COMMAND))
def wave(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/wave").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗔𝗰𝗲𝗻𝗮 𝗽𝗿𝗮 👋 {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/wave").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} 𝗔𝗰𝗲𝗻𝗮 👋")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_BLUSH_COMMAND))
def blush(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/blush").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗰𝗼𝗿𝗮 💔 𝗽𝗿𝗮 {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/blush").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} 𝗰𝗼𝗿𝗮 💔")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_NEKO_COMMAND))
def neko(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/neko").json()
        url = api["results"][0]["url"]
        reply.reply_photo(url, caption=f"𝗡𝗲𝗸𝗼 𝗱𝗲 🐱💤 {reply.from_user.first_name}")
    else:
        api = requests.get("https://nekos.best/api/v2/neko").json()
        url = api["results"][0]["url"]
        m.reply_photo(url, caption=f"𝗡𝗲𝗸𝗼 𝗱𝗲 🐱💤 {m.from_user.first_name}")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_DANCE_COMMAND))
def dance(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/dance").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 💃 𝗱𝗮𝗻ç𝗮 𝗽𝗿𝗮 🕺 {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/dance").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"𝗗𝗮𝗻𝗰̧𝗮 𝗺𝗮𝗻𝗮 💃🎶")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_BAKA_COMMAND))
def baka(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/baka").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗕𝗮𝗸𝗮 𝗽𝗿𝗮 💢 {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/baka").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} 𝗕𝗮𝗸𝗮 💢")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_BORE_COMMAND))
def bore(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/bored").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗖𝗼𝗺 𝘁é𝗱𝗶𝗼 𝗱𝗲 😒 {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/bored").json()
        url = api["results"][0]["url"]
        m.reply_animation(
            animation=url, caption=f"{m.from_user.first_name} 𝗖𝗼𝗺 𝘁é𝗱𝗶𝗼 😒"
        )


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_LAUGH_COMMAND))
def laugh(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/laugh").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗿𝗶 𝗱𝗲 😂 {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/laugh").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} 𝗿𝗶 𝗵𝗶𝗵𝗶 🤭")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_SMUG_COMMAND))
def smug(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/smug").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗦𝗲 𝗮𝗰𝗵𝗮 𝗱𝗶 🤔💭 {reply.from_user.first_name}  🌈",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/smug").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} 𝗦𝗲 𝗮𝗰𝗵𝗮 🤔💭")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_THUMBSUP_COMMAND))
def thumbsup(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/thumbsup").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗖𝗼𝗻𝗰𝗼𝗿𝗱𝗼 𝗰𝗼𝗺 👍🏼 {reply.from_user.first_name}  🌈",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/thumbsup").json()
        url = api["results"][0]["url"]
        m.reply_animation(
            animation=url, caption=f"{m.from_user.first_name} 𝗖𝗼𝗻𝗰𝗼𝗿𝗱𝗼 👍🏼"
        )


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_SHOOT_COMMAND))
def shoot(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/shoot").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗔𝘁𝗶𝗿𝗮 𝗲𝗺 🔫 {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/shoot").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"𝗔𝘁𝗶𝗿𝗮 🔫 {m.from_user.first_name}")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_TICKLE_COMMAND))
def tickle(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/tickle").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗙𝗮𝘇 𝗰𝗼́𝗰𝗲𝗴𝗮𝘀 𝗲𝗺 😄✋🪶 {reply.from_user.first_name}  🌈",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/tickle").json()
        url = api["results"][0]["url"]
        m.reply_animation(
            animation=url, caption=f"𝗙𝗮𝘇 𝗰𝗼́𝗰𝗲𝗴𝗮𝘀 {m.from_user.first_name}  😄✋🪶"
        )


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_FEED_COMMAND))
def feed(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/feed").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗖𝗼𝗺𝗲 🍽️🍴 {reply.from_user.first_name}  🌈",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/feed").json()
        url = api["results"][0]["url"]
        m.reply_animation(
            animation=url, caption=f"{m.from_user.first_name} 𝗖𝘂𝗺 𝗳𝗼𝗺𝗶 🍴😋"
        )


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_THINK_COMMAND))
def think(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/think").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗣𝗲𝗻𝘀𝗮 𝘀𝗼𝗯𝗿𝗲 🤔💭🧠 𝘂 {reply.from_user.first_name} ",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/think").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} 𝗣𝗲𝗻𝘀𝗮 🤔💭🧠")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_WINK_COMMAND))
def wink(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/wink").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗣𝗶𝘀𝗰𝗮 𝗽𝗿𝗮 😉 {reply.from_user.first_name}  🌈",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/wink").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} 𝗣𝗶𝘀𝗰𝗮 😉")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_SLEEP_COMMAND))
def sleep(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/sleep").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url, caption=f"𝗩𝗮𝗺𝘂 𝗱𝘂𝗿𝗺𝗶 𝗺𝗮𝗻𝗮 🌙💤 {reply.from_user.first_name}  🌈"
        )
    else:
        api = requests.get("https://nekos.best/api/v2/sleep").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} 𝗱𝘂𝗿𝗺𝗶 🌙💤")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_PUNCH_COMMAND))
def punch(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://nekos.best/api/v2/punch").json()
        url = api["results"][0]["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗦𝗼𝗰𝗮 𝘂 👊🆙 {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://nekos.best/api/v2/punch").json()
        url = api["results"][0]["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} ಠ‿ಠ 𝗦𝗼𝗰𝗮 👊")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_CRY_COMMAND))
def cry(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://waifu.pics/api/sfw/cry").json()
        url = api["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗖𝗵𝗼𝗿𝗮 😭 𝗽𝗼𝗲 😢 {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://waifu.pics/api/sfw/cry").json()
        url = api["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} 𝗖𝗵𝗼𝗿𝗮 😭")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_KILL_COMMAND))
def kill(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://waifu.pics/api/sfw/kill").json()
        url = api["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} mata 🌳🔪 {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://waifu.pics/api/sfw/kill").json()
        url = api["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} mata 🌳🔪")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_SMILE_COMMAND))
def smile(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://waifu.pics/api/sfw/smile").json()
        url = api["url"]
        reply.reply_animation(
            url,
            caption=f"{m.from_user.first_name} 𝗦𝗼𝗿𝗿𝗶 𝗱𝗶 😊✨ {reply.from_user.first_name}",
        )
    else:
        api = requests.get("https://waifu.pics/api/sfw/smile").json()
        url = api["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} 𝗦𝗼𝗿𝗿𝗶 😊")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_HIGHFIVE_COMMAND))
def highfive(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://waifu.pics/api/sfw/highfive").json()
        url = api["url"]
        reply.reply_animation(url)
    else:
        api = requests.get("https://waifu.pics/api/sfw/highfive").json()
        url = api["url"]
        m.reply_animation(animation=url)


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_SLAP_COMMAND))
def slap(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://waifu.pics/api/sfw/slap").json()
        url = api["url"]
        name1 = reply.from_user.first_name
        name2 = m.from_user.first_name
        reply.reply_animation(
            url, caption="{} (((;ꏿ_ꏿ;))) 𝗧𝗮𝗽𝗮𝘀 👋 {} ಠಗಠ".format(name2, name1)
        )
    else:
        api = requests.get("https://waifu.pics/api/sfw/slap").json()
        url = api["url"]
        m.reply_animation(url, caption=f"𝗧𝗮𝗽𝗮𝘀 👋 {m.from_user.first_name} ಠ‿ಠ")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_HUG_COMMAND))
def hug(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://waifu.pics/api/sfw/hug").json()
        url = api["url"]
        name1 = reply.from_user.first_name
        name2 = m.from_user.first_name
        reply.reply_animation(
            url, caption="{} ( ◜‿◝ )♡ 𝗔𝗯𝗿𝗮𝗰𝗲𝘀 🤗👐 {} ( ╹▽╹ )".format(name2, name1)
        )
    else:
        api = requests.get("https://waifu.pics/api/sfw/hug").json()
        url = api["url"]
        m.reply_animation(animation=url, caption=f"{m.from_user.first_name} 𝗯𝗿𝗮𝗰𝗲𝘀 🤗👐")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_PAT_COMMAND))
def pat(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://waifu.pics/api/sfw/pat").json()
        url = api["url"]
        name1 = reply.from_user.first_name
        name2 = m.from_user.first_name
        reply.reply_animation(
            url, caption="{} ( ◜‿◝ )♡ 𝗔𝗺𝗼𝗲𝘀 💖🌹 {} ( ╹▽╹ )".format(name2, name1)
        )
    else:
        api = requests.get("https://waifu.pics/api/sfw/pat").json()
        url = api["url"]
        m.reply_animation(animation=url, caption=f"𝗔𝗺𝗼𝗲𝘀 💖🌹 {m.from_user.first_name}")


# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(NEKO_WAIFU_COMMAND))
def waifu(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://waifu.pics/api/sfw/waifu").json()
        url = api["url"]
        reply.reply_photo(url, caption=f"𝗪𝗮𝗶𝗳𝘂 𝗱𝗲 💕👘💮 {reply.from_user.first_name}")
    else:
        api = requests.get("https://waifu.pics/api/sfw/waifu").json()
        url = api["url"]
        m.reply_photo(photo=url, caption=f"𝗪𝗮𝗶𝗳𝘂 𝗱𝗲 💕👘💮 {m.from_user.first_name}")


# --------------------------------------------------------------------------------- #


# only for pv chat
@app.on_message(filters.command("trap"))
def trap(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://waifu.pics/api/nsfw/trap").json()
        url = api["url"]
        reply.reply_photo(url, caption=f"𝗧𝗿𝗮𝗽 𝗽𝗮𝗿𝗮 🪤🚫 {reply.from_user.first_name}")
    else:
        api = requests.get("https://waifu.pics/api/nsfw/trap").json()
        url = api["url"]
        m.reply_photo(photo=url, caption=f"𝗧𝗿𝗮𝗽 🪤🚫 {m.from_user.first_name}")


@app.on_message(filters.command("mamada"))
def mamada(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://waifu.pics/api/nsfw/blowjob").json()
        url = api["url"]
        reply.reply_animation(
            animation=url, caption=f"𝗠𝗮𝗺𝗮𝗻𝗱𝗼 𝗼 🍼 {reply.from_user.first_name}"
        )
    else:
        api = requests.get("https://waifu.pics/api/nsfw/blowjob").json()
        url = api["url"]
        m.reply_animation(animation=url, caption=f"𝗠𝗮𝗺𝗮𝗻𝗱𝗼 🍼 {m.from_user.first_name}")


@app.on_message(filters.command("neko_xxx"))
def neko_xxx(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://waifu.pics/api/nsfw/neko").json()
        url = api["url"]
        reply.reply_photo(url, caption=f"𝗡𝗲𝗸𝗼 {reply.from_user.first_name}")
    else:
        api = requests.get("https://waifu.pics/api/nsfw/neko").json()
        url = api["url"]
        m.reply_photo(photo=url, caption=f"𝗡𝗲𝗸𝗼 {m.from_user.first_name}")


@app.on_message(filters.command("wifu_xxx"))
def wifu_xxx(_, m: Message):
    reply = m.reply_to_message
    if reply:
        api = requests.get("https://waifu.pics/api/nsfw/waifu").json()
        url = api["url"]
        reply.reply_photo(url, caption=f"𝗪𝗶𝗳𝘂 𝗽𝗮𝗿𝗮 {reply.from_user.first_name}")
    else:
        api = requests.get("https://waifu.pics/api/nsfw/waifu").json()
        url = api["url"]
        m.reply_photo(photo=url, caption=f"𝗪𝗶𝗳𝘂 𝗱𝗲 {m.from_user.first_name}")


# --------------------------------------------------------------------------------- #
@app.on_message(filters.regex(r"^amoe"))
async def love(_, message):
    await message.reply("𝗮𝗺𝗼𝗲.. 𝗺𝗮𝗻𝗮 💖👭🌈")
