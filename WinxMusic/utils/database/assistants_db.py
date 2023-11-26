import random
from typing import Dict

from WinxMusic import userbot
from WinxMusic.core.mongo import mongodb

assistants_db = mongodb.assistants
assistant_dict: Dict[int, int] = {}


async def get_assistant_number(chat_id: int) -> int:
    assistant = assistant_dict.get(chat_id)
    return assistant


async def get_client(assistant: int):
    if int(assistant) == 1:
        return userbot.one
    elif int(assistant) == 2:
        return userbot.two
    elif int(assistant) == 3:
        return userbot.three
    elif int(assistant) == 4:
        return userbot.four
    elif int(assistant) == 5:
        return userbot.five
    elif int(assistant) == 6:
        return userbot.six
    elif int(assistant) == 7:
        return userbot.seven
    elif int(assistant) == 8:
        return userbot.eight
    elif int(assistant) == 9:
        return userbot.nine
    elif int(assistant) == 10:
        return userbot.ten


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
    if int(assis) == 1:
        return self.one
    elif int(assis) == 2:
        return self.two
    elif int(assis) == 3:
        return self.three
    elif int(assis) == 4:
        return self.four
    elif int(assis) == 5:
        return self.five
    elif int(assis) == 6:
        return self.six
    elif int(assis) == 7:
        return self.seven
    elif int(assis) == 8:
        return self.eight
    elif int(assis) == 9:
        return self.nine
    elif int(assis) == 10:
        return self.ten
