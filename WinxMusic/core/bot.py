from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class Winx(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="WinxMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"🚀<u><b>➜ {self.mention} 𝗕𝗼𝘁 𝗶𝗻𝗶𝗰𝗶𝗮𝗱𝗼:</b></u>🚀\n\n𝗜𝗗: <code>{self.id}</code>\n"
                f"𝗡𝗼𝗺𝗲: {self.name}\n𝗨𝘀𝘂𝗮́𝗿𝗶𝗼: @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log "
                "group/channel."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote your bot as an admin in your log group/channel."
            )
            exit()
        if config.SET_CMDS == str(True):
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("ping", "Veja se o bot está online"),
                        BotCommand("play", "Reproduz a música solicitada"),
                        BotCommand("skip", "Pula a música atual"),
                        BotCommand("pause", "Pausa a música atual"),
                        BotCommand("resume", "Retoma a música atual"),
                        BotCommand("end", "Para a música atual e limpa a fila"),
                        BotCommand("shuffle", "Embaralha a fila de músicas"),
                        BotCommand("playmode", "Alterna entre os modos de reprodução"),
                        BotCommand("settings", "Abre o menu de configurações"),
                        BotCommand("wifu", "Envia uma imagem aleatória de anime"),
                        BotCommand("waifu", "Envia um comando waifu"),
                        BotCommand("couple", "Envia um comando de casal do dia"),
                        BotCommand("cuddle", "Envia um comando de carinho"),
                        BotCommand("shrug", "Envia um comando de dar de ombros"),
                        BotCommand("poke", "Envia um comando de cutucar"),
                        BotCommand("facepalm", "Envia um comando de facepalm"),
                        BotCommand("stare", "Envia um comando de olhar fixamente"),
                        BotCommand("pout", "Envia um comando de fazer bico"),
                        BotCommand("handhold", "Envia um comando de segurar a mão"),
                        BotCommand("wave", "Envia um comando de acenar"),
                        BotCommand("blush", "Envia um comando de corar"),
                        BotCommand("neko", "Envia um comando neko"),
                        BotCommand("dance", "Envia um comando de dançar"),
                        BotCommand("baka", "Envia um comando de insulto leve"),
                        BotCommand("bore", "Envia um comando de tédio"),
                        BotCommand("laugh", "Envia um comando de risada"),
                        BotCommand("smug", "Envia um comando de arrogância"),
                        BotCommand("thumbsup", "Envia um comando de joinha"),
                        BotCommand("shoot", "Envia um comando de atirar"),
                        BotCommand("tickle", "Envia um comando de cócegas"),
                        BotCommand("feed", "Envia um comando de alimentar"),
                        BotCommand("think", "Envia um comando de pensar"),
                        BotCommand("wink", "Envia um comando de piscar"),
                        BotCommand("sleep", "Envia um comando de dormir"),
                        BotCommand("punch", "Envia um comando de soco"),
                        BotCommand("cry", "Envia um comando de chorar"),
                        BotCommand("kill", "Envia um comando de matar"),
                        BotCommand("smile", "Envia um comando de sorrir"),
                        BotCommand("highfive", "Envia um comando de toca aqui"),
                        BotCommand("slap", "Envia um comando de tapa"),
                        BotCommand("hug", "Envia um comando de abraço"),
                        BotCommand("pat", "Envia um comando de afagar"),
                    ]
                )
            except:
                pass
        else:
            pass

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
