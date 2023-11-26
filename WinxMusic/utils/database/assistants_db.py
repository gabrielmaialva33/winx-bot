import random
from typing import Dict

from WinxMusic import userbot
from WinxMusic.core.mongo import mongodb

assistants_db = mongodb.assistants
assistant_dict: Dict[int, int] = {}


async def get_assistant_number(chat_id: int) -> int:
    assistant = assistant_dict.get(int(chat_id))
    return assistant


async def get_client(assistant: int) -> userbot:
    assistant_clients = {
        1: userbot.one,
        2: userbot.two,
        3: userbot.three,
        4: userbot.four,
        5: userbot.five,
        6: userbot.six,
        7: userbot.seven,
        8: userbot.eight,
        9: userbot.nine,
        10: userbot.ten,
    }
    return assistant_clients[int(assistant)]


async def set_assistant_new(chat_id, number):
    number = int(number)
    await assistants_db.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": number}},
        upsert=True,
    )


async def set_assistant(chat_id):
    from WinxMusic.core.userbot import assistants

    ran_assistant = random.choice(assistants)
    assistant_dict[chat_id] = ran_assistant
    await assistants_db.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": ran_assistant}},
        upsert=True,
    )
    userbot = await get_client(ran_assistant)
    return userbot


async def get_assistant(chat_id: int) -> str:
    from WinxMusic.core.userbot import assistants

    assistant = assistant_dict.get(chat_id)
    if not assistant:
        db_assistant = await assistants_db.find_one({"chat_id": chat_id})
        if not db_assistant:
            userbot = await set_assistant(chat_id)
            return userbot
        else:
            got_assis = db_assistant["assistant"]
            if got_assis in assistants:
                assistant_dict[chat_id] = got_assis
                userbot = await get_client(got_assis)
                return userbot
            else:
                userbot = await set_assistant(chat_id)
                return userbot
    else:
        if assistant in assistants:
            userbot = await get_client(assistant)
            return userbot
        else:
            userbot = await set_assistant(chat_id)
            return userbot


async def set_calls_assistant(chat_id):
    from WinxMusic.core.userbot import assistants

    ran_assistant = random.choice(assistants)
    assistant_dict[chat_id] = ran_assistant
    await assistants_db.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": ran_assistant}},
        upsert=True,
    )
    return ran_assistant


async def group_assistant(self, chat_id: int) -> int:
    from WinxMusic.core.userbot import assistants

    assistant = assistant_dict.get(chat_id)
    if not assistant:
        db_assistant = await assistants_db.find_one({"chat_id": chat_id})
        if not db_assistant:
            assis = await set_calls_assistant(chat_id)
        else:
            assis = db_assistant["assistant"]
            if assis in assistants:
                assistant_dict[chat_id] = assis
                assis = assis
            else:
                assis = await set_calls_assistant(chat_id)
    else:
        if assistant in assistants:
            assis = assistant
        else:
            assis = await set_calls_assistant(chat_id)
    self_clients = {
        1: self.one,
        2: self.two,
        3: self.three,
        4: self.four,
        5: self.five,
        6: self.six,
        7: self.seven,
        8: self.eight,
        9: self.nine,
        10: self.ten,
    }
    return self_clients[int(assis)]
