import asyncio

from pyrogram import Client as c

API_ID = input("\n➜ 𝙲𝚘𝚕𝚘𝚚𝚞𝚎 𝚜𝚎𝚞 𝙰𝙿𝙸_𝙸𝙳: 🔑\n➜ ")
API_HASH = input("\n➜ 𝙲𝚘𝚕𝚘𝚚𝚞𝚎 𝚜𝚞𝚊 𝙰𝙿𝙸_𝙷𝙰𝚂𝙷: 🔒\n➜ ")

print("\n\n➜ 𝙲𝚘𝚕𝚘𝚚𝚞𝚎 𝚘 𝚗𝚞𝚖𝚎𝚛𝚘 𝚍𝚎 𝚝𝚎𝚕𝚎𝚏𝚘𝚗𝚎 𝚚𝚞𝚊𝚗𝚍𝚘 𝚜𝚘𝚕𝚒𝚌𝚒𝚝𝚊𝚍𝚘. 📞\n\n")

i = c("WinxString", in_memory=True, api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\n𝗔𝗤𝗨𝗜 𝗘𝗦𝗧Á 𝗢 𝗦𝗘𝗨 𝗦𝗧𝗥𝗜𝗡𝗚 𝗗𝗘 𝗦𝗘𝗦𝗦Ã𝗢, 𝗖𝗢𝗣𝗜𝗘, 𝗡Ã𝗢 𝗖𝗢𝗠𝗣𝗔𝗥𝗧𝗜𝗟𝗛𝗘!! 📋❌\n")
    print(f"\n{ss}\n")


asyncio.run(main())
