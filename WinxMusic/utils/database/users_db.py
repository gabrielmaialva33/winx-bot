from WinxMusic.core.mongo import mongodb

users_db = mongodb.tgusersdb


async def is_served_user(user_id: int) -> bool:
    user = await users_db.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def get_served_users() -> list:
    users_list = []
    async for user in users_db.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list


async def add_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await users_db.insert_one({"user_id": user_id})


async def remove_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if not is_served:
        return
    return await users_db.delete_one({"user_id": user_id})
