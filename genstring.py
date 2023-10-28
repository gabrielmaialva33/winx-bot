import asyncio

from pyrogram import Client as c

API_ID = input("\n➜ 𝗜𝗻𝘀𝗶𝗿𝗮 𝘀𝘂𝗮 𝗔𝗣𝗜_𝗜𝗗: 🔑\n > ")
API_HASH = input("\n➜ 𝗜𝗻𝘀𝗶𝗿𝗮 𝘀𝘂𝗮 𝗔𝗣𝗜_𝗛𝗔𝗦𝗛: 🔒\n > ")

print("\n\n➜ 𝗜𝗻𝘀𝗶𝗿𝗮 𝗼 𝗻𝘂𝗺𝗲𝗿𝗼 𝗱𝗼 𝘁𝗲𝗹𝗲𝗳𝗼𝗻𝗲 𝗾𝘂𝗮𝗻𝗱𝗼 𝘀𝗼𝗹𝗶𝗰𝗶𝘁𝗮𝗱𝗼. 📞\n\n")

i = c("WinxString", in_memory=True, api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\n𝗔𝗤𝗨𝗜 𝗘𝗦𝗧Á 𝗢 𝗦𝗘𝗨 𝗦𝗧𝗥𝗜𝗡𝗚 𝗗𝗘 𝗦𝗘𝗦𝗦Ã𝗢, 𝗖𝗢𝗣𝗜𝗘, 𝗡Ã𝗢 𝗖𝗢𝗠𝗣𝗔𝗥𝗧𝗜𝗟𝗛𝗘!! 📋❌\n")
    print(f"\n{ss}\n")


asyncio.run(main())
