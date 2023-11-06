import asyncio

from pyrogram import Client as c

API_ID = input("\n➜ Coloque seu API_ID: 🔑\n➜ ")
API_HASH = input("\n➜ Coloque seu API_HASH: 🔒\n➜ ")

print("\n\n➜ O numero de telefone 📞\n\n")

i = c("WinxString", in_memory=True, api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\nSua session 📋❌\n")
    print(f"\n{ss}\n")


asyncio.run(main())
