from typing import Any, Dict, List, Union

from WinxMusic.core.mongo import mongodb

chats_db = mongodb.chats


async def get_served_chats() -> list:
    chats_list = []
    async for chat in chats_db.find({"chat_id": {"$lt": 0}}):
        chats_list.append(chat)
    return chats_list


async def is_served_chat(chat_id: int) -> bool:
    chat = await chats_db.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await chats_db.insert_one({"chat_id": chat_id})


async def remove_served_chat(chat_id: int):
    return await chats_db.delete_one({"chat_id": chat_id})


async def get_chat(chat_id: int) -> Union[Dict[str, Any], None]:
    return await chats_db.find_one({"chat_id": chat_id})

