from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class Winx(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting Bot...")
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
        await self.setup_bot_properties()
        await self.log_bot_start()
        await self.check_bot_admin_status()
        await self.configure_bot_commands()

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()

    async def setup_bot_properties(self):
        self.id = self.me.id
        self.name = f"{self.me.first_name} {self.me.last_name or ''}"
        self.username = self.me.username
        self.mention = self.me.mention

    async def log_bot_start(self):
        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"🚀<u><b>➜ {self.mention} Bot iniciado:</b></u>🚀\n\n"
                f"ID: <code>{self.id}</code>\nNome: {self.name}\nUsuário: @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot falhou ao acessar o grupo/canal de log. Certifique-se de que adicionou o bot ao seu grupo/canal "
                "de log."
            )
            raise
        except Exception as e:
            LOGGER(__name__).error(
                f"Falha ao acessar o grupo/canal de log. Motivo: {type(e).__name__}."
            )
            raise

    async def check_bot_admin_status(self):
        chat_member = await self.get_chat_member(config.LOGGER_ID, self.id)
        if chat_member.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Por favor, promova seu bot a admin no seu grupo/canal de log."
            )
            raise PermissionError("Bot não é administrador no grupo/canal de log.")

    async def configure_bot_commands(self):
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
                        BotCommand("gpt", "Chat com GPT-3"),
                        BotCommand("bard", "Chat com Bard"),
                        BotCommand("llm", "Chat com os modelos LLAMA"),
                        BotCommand("draw", "Desenhe com a AI"),
                    ]
                )
            except Exception as e:
                LOGGER(__name__).warning(
                    f"Não foi possível configurar os comandos do bot: {e}"
                )
