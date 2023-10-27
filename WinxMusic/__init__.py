from WinxMusic.core.bot import Winx
from WinxMusic.core.dir import dirr
from WinxMusic.core.git import git
from WinxMusic.core.userbot import Userbot
from WinxMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Winx()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
