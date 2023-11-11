from pyrogram import *
from SafoneAPI import api

from ... import *


@app.on_message(filters.command(["bin", "ccbin", "bininfo"], [".", "!", "/"]))
async def check_ccbin(_client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            f"<b>Por favor, insira um número de BIN válido!</b>"
            f"\n\n<b>Exemplo:</b> <code>/bin 123456</code>"
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("<b>🔎 Verificando BIN...</b>")
    bin = message.text.split(None, 1)[1]
    if len(bin) < 6:
        return await aux.edit("<b>❌ BIN inválido!</b>")
    try:
        resp = await api.SafoneAPI.bininfo(bin)
        await aux.edit(
            f"""
<b>💠 Bin Full Details:</b>

<b>🏦 Bank:</b> <tt>{resp.bank}</tt>
<b>💳 Bin:</b> <tt>{resp.bin}</tt>
<b>🏡 Country:</b> <tt>{resp.country}</tt>
<b>🇮🇳 Flag:</b> <tt>{resp.flag}</tt>
<b>🧿 ISO:</b> <tt>{resp.iso}</tt>
<b>⏳ Level:</b> <tt>{resp.level}</tt>
<b>🔴 Prepaid:</b> <tt>{resp.prepaid}</tt>
<b>🆔 Type:</b> <tt>{resp.type}</tt>
<b>ℹ️ Vendor:</b> <tt>{resp.vendor}</tt>"""
        )
    except:
        return await aux.edit(
            f"""
🚫 BIN não encontrada! Por favor, insira um BIN válido para verificar."""
        )
