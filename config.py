import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

OPEN_AI_API_KEY = getenv("OPEN_AI_API_KEY", None)

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @mrootx on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID"))

# Set a Playlist Limit
QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "10"))

LEAVE_TIME = int(getenv("LEAVE_TIME", "3600"))

SET_CMDS = getenv("SET_CMDS", "False")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/gabrielmaialva33/winx-bot.git",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/clubdaswinxcanal"
)  # Example:- https://t.me/politicament
SUPPORT_CHAT = getenv(
    "SUPPORT_GROUP", "https://t.me/winxmusicsupport"
)  # Example:- https://t.me/politicament

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
STRING8 = getenv("STRING_SESSION8", None)
STRING9 = getenv("STRING_SESSION9", None)
STRING10 = getenv("STRING_SESSION10", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Images
START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://64.media.tumblr.com/b20a9df719f8420ac7aa02ece2cb1774/5f8ef1a042cf9e6b-7f/s540x810/eba21bbdb525e72f84be27d439c156b4dfa6b31a.gifv",
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://64.media.tumblr.com/ea7bbbc05fe47c0306c2ac389eccc252/7724188deed06fee-a2/s1280x1920/3e5de4c6847843b79902a50a0873a58325551d55.gifv",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://64.media.tumblr.com/73084dccbeffd73655bb3a07cef7904a/ca2e3db2a56b2f2d-71/s540x810/747f6f9a572be30f47bb428e51aa66d9c2435b35.gifv",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://64.media.tumblr.com/ac0bd0dbb6d9e3c7471630584e58b668/42dbca30b09f38f4-36/s1280x1920/ec602883a8242946698b201505bc7a47ac2f6afe.gifv",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://64.media.tumblr.com/a98891c693052dd873231ab51b721421/d6aa089c4433b10c-24/s1280x1920/1d296936e8fa25471b51761e64fbeeaf0c28fc8a.gifv",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://64.media.tumblr.com/79bb5c54237323c17c93af4c3c83671b/667b875d0810726a-86/s1280x1920/018a7062497c7599991eac83a4f41844484e90e7.gifv",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://64.media.tumblr.com/79bb5c54237323c17c93af4c3c83671b/667b875d0810726a-86/s1280x1920/018a7062497c7599991eac83a4f41844484e90e7.gifv",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://64.media.tumblr.com/ea7bbbc05fe47c0306c2ac389eccc252/7724188deed06fee-a2/s1280x1920/3e5de4c6847843b79902a50a0873a58325551d55.gifv",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://64.media.tumblr.com/ea7bbbc05fe47c0306c2ac389eccc252/7724188deed06fee-a2/s1280x1920/3e5de4c6847843b79902a50a0873a58325551d55.gifv",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://64.media.tumblr.com/c39b07d55fbdff89661056be8bd08dbd/df2251522787e803-87/s1280x1920/40ae16b0ab0adadc2914146b115ab4ba0480863e.gifv",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://64.media.tumblr.com/73084dccbeffd73655bb3a07cef7904a/ca2e3db2a56b2f2d-71/s1280x1920/173c28fc197aef873f69df081e0671c35eacc9fb.gifv",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://64.media.tumblr.com/73084dccbeffd73655bb3a07cef7904a/ca2e3db2a56b2f2d-71/s1280x1920/173c28fc197aef873f69df081e0671c35eacc9fb.gifv",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://64.media.tumblr.com/73084dccbeffd73655bb3a07cef7904a/ca2e3db2a56b2f2d-71/s1280x1920/173c28fc197aef873f69df081e0671c35eacc9fb.gifv",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
