from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="WinxAssistant1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="WinxAssistant2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="WinxAssistant3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="WinxAssistant4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="WinxAssistant5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )
        self.six = Client(
            name="WinxAssistant6",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING6),
            no_updates=True,
        )
        self.seven = Client(
            name="WinxAssistant7",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING7),
            no_updates=True,
        )
        self.eight = Client(
            name="WinxAssistant8",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING8),
            no_updates=True,
        )
        self.nine = Client(
            name="WinxAssistant9",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING9),
            no_updates=True,
        )
        self.ten = Client(
            name="WinxAssistant10",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING10),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        if config.STRING1:
            await self.one.start()
            assistants.append(1)

            await self.one.join_chat("@winxbotx")
            await self.one.join_chat("@winxmusicsupport")
            await self.one.join_chat("@cinewinx")
            await self.one.join_chat("@clubdaswinxcanal")
            await self.one.join_chat("@cinewinxcoments")

            try:
                await self.one.send_message(config.LOGGER_ID, "𝗔𝘀𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗲 𝗜𝗻𝗶𝗰𝗶𝗮𝗱𝗮 🪄")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 1 has failed to access the log Group. Make sure that you have added your "
                    "assistant to your log group and promoted as admin!"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

        if config.STRING2:
            await self.two.start()
            assistants.append(2)

            await self.two.join_chat("@winxbotx")
            await self.two.join_chat("@winxmusicsupport")
            await self.two.join_chat("@cinewinx")
            await self.two.join_chat("@clubdaswinxcanal")
            await self.two.join_chat("@cinewinxcoments")

            try:
                await self.two.send_message(config.LOGGER_ID, "𝗔𝘀𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗲 𝗜𝗻𝗶𝗰𝗶𝗮𝗱𝗮 🪄")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your "
                    "assistant to your log group and promoted as admin!"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")

        if config.STRING3:
            await self.three.start()
            assistants.append(3)

            await self.three.join_chat("@winxbotx")
            await self.three.join_chat("@winxmusicsupport")
            await self.three.join_chat("@cinewinx")
            await self.three.join_chat("@clubdaswinxcanal")
            await self.three.join_chat("@cinewinxcoments")

            try:
                await self.three.send_message(config.LOGGER_ID, "𝗔𝘀𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗲 𝗜𝗻𝗶𝗰𝗶𝗮𝗱𝗮 🪄")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your "
                    "assistant to your log group and promoted as admin!"
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")

        if config.STRING4:
            await self.four.start()
            assistants.append(4)

            await self.four.join_chat("@winxbotx")
            await self.four.join_chat("@winxmusicsupport")
            await self.four.join_chat("@cinewinx")
            await self.four.join_chat("@clubdaswinxcanal")
            await self.four.join_chat("@cinewinxcoments")

            try:
                await self.four.send_message(config.LOGGER_ID, "𝗔𝘀𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗲 𝗜𝗻𝗶𝗰𝗶𝗮𝗱𝗮 🪄")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your "
                    "assistant to your log group and promoted as admin!"
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")

        if config.STRING5:
            await self.five.start()
            assistants.append(5)

            await self.five.join_chat("@winxbotx")
            await self.five.join_chat("@winxmusicsupport")
            await self.five.join_chat("@cinewinx")
            await self.five.join_chat("@clubdaswinxcanal")
            await self.five.join_chat("@cinewinxcoments")

            try:
                await self.five.send_message(config.LOGGER_ID, "𝗔𝘀𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗲 𝗜𝗻𝗶𝗰𝗶𝗮𝗱𝗮 🪄")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your "
                    "assistant to your log group and promoted as admin!"
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")

        if config.STRING6:
            await self.six.start()
            assistants.append(6)

            await self.six.join_chat("@winxbotx")
            await self.six.join_chat("@winxmusicsupport")
            await self.six.join_chat("@cinewinx")
            await self.six.join_chat("@clubdaswinxcanal")
            await self.six.join_chat("@cinewinxcoments")

            try:
                await self.six.send_message(config.LOGGER_ID, "𝗔𝘀𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗲 𝗜𝗻𝗶𝗰𝗶𝗮𝗱𝗮 🪄")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 6 has failed to access the log Group. Make sure that you have added your "
                    "assistant to your log group and promoted as admin!"
                )
                exit()
            self.six.id = self.six.me.id
            self.six.name = self.six.me.mention
            self.six.username = self.six.me.username
            assistantids.append(self.six.id)
            LOGGER(__name__).info(f"Assistant Six Started as {self.six.name}")

        if config.STRING7:
            await self.seven.start()
            assistants.append(7)

            await self.seven.join_chat("@winxbotx")
            await self.seven.join_chat("@winxmusicsupport")
            await self.seven.join_chat("@cinewinx")
            await self.seven.join_chat("@clubdaswinxcanal")
            await self.seven.join_chat("@cinewinxcoments")

            try:
                await self.seven.send_message(config.LOGGER_ID, "𝗔𝘀𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗲 𝗜𝗻𝗶𝗰𝗶𝗮𝗱𝗮 🪄")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 7 has failed to access the log Group. Make sure that you have added your "
                    "assistant to your log group and promoted as admin!"
                )
                exit()
            self.seven.id = self.seven.me.id
            self.seven.name = self.seven.me.mention
            self.seven.username = self.seven.me.username
            assistantids.append(self.seven.id)
            LOGGER(__name__).info(f"Assistant Seven Started as {self.seven.name}")

        if config.STRING8:
            await self.eight.start()
            assistants.append(8)

            await self.eight.join_chat("@winxbotx")
            await self.eight.join_chat("@winxmusicsupport")
            await self.eight.join_chat("@cinewinx")
            await self.eight.join_chat("@clubdaswinxcanal")
            await self.eight.join_chat("@cinewinxcoments")

            try:
                await self.eight.send_message(config.LOGGER_ID, "𝗔𝘀𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗲 𝗜𝗻𝗶𝗰𝗶𝗮𝗱𝗮 🪄")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 8 has failed to access the log Group. Make sure that you have added your "
                    "assistant to your log group and promoted as admin!"
                )
                exit()
            self.eight.id = self.eight.me.id
            self.eight.name = self.eight.me.mention
            self.eight.username = self.eight.me.username
            assistantids.append(self.eight.id)
            LOGGER(__name__).info(f"Assistant Eight Started as {self.eight.name}")

        if config.STRING9:
            await self.nine.start()
            assistants.append(9)

            await self.nine.join_chat("@winxbotx")
            await self.nine.join_chat("@winxmusicsupport")
            await self.nine.join_chat("@cinewinx")
            await self.nine.join_chat("@clubdaswinxcanal")
            await self.nine.join_chat("@cinewinxcoments")

            try:
                await self.nine.send_message(config.LOGGER_ID, "𝗔𝘀𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗲 𝗜𝗻𝗶𝗰𝗶𝗮𝗱𝗮 🪄")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 9 has failed to access the log Group. Make sure that you have added your "
                    "assistant to your log group and promoted as admin!"
                )
                exit()
            self.nine.id = self.nine.me.id
            self.nine.name = self.nine.me.mention
            self.nine.username = self.nine.me.username
            assistantids.append(self.nine.id)
            LOGGER(__name__).info(f"Assistant Nine Started as {self.nine.name}")

        if config.STRING10:
            await self.ten.start()
            assistants.append(10)

            await self.ten.join_chat("@winxbotx")
            await self.ten.join_chat("@winxmusicsupport")
            await self.ten.join_chat("@cinewinx")
            await self.ten.join_chat("@clubdaswinxcanal")
            await self.ten.join_chat("@cinewinxcoments")

            try:
                await self.ten.send_message(config.LOGGER_ID, "𝗔𝘀𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗲 𝗜𝗻𝗶𝗰𝗶𝗮𝗱𝗮 🪄")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 10 has failed to access the log Group. Make sure that you have added your "
                    "assistant to your log group and promoted as admin!"
                )
                exit()
            self.ten.id = self.ten.me.id
            self.ten.name = self.ten.me.mention
            self.ten.username = self.ten.me.username
            assistantids.append(self.ten.id)
            LOGGER(__name__).info(f"Assistant Ten Started as {self.ten.name}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
            if config.STRING6:
                await self.six.stop()
            if config.STRING7:
                await self.seven.stop()
            if config.STRING8:
                await self.eight.stop()
            if config.STRING9:
                await self.nine.stop()
            if config.STRING10:
                await self.ten.stop()
        except:
            pass
