from pyrogram import *
from SafoneAPI import SafoneAPI
from ... import *

api = SafoneAPI()


@app.on_message(filters.command(["bin", "ccbin", "bininfo"], [".", "!", "/"]))
async def check_ccbin(_client, message):
    bin_number = get_bin_number(message)
    if not bin_number:
        return await message.reply_text(
            "<b>Por favor, insira um número de BIN válido!</b>"
            "\n\n<b>Exemplo:</b> <code>/bin 536698</code>"
        )

    await message.delete()
    reply_message = await message.reply_text("<b>🔎 Verificando BIN...</b>")

    try:
        bin_info = await fetch_bin_info(bin_number)
        await reply_message.edit(bin_info)
    except Exception as e:
        LOGGER(__name__).error(e)
        await reply_message.edit(
            "🚫 BIN não encontrada!"
        )


def get_bin_number(message):
    """Extrai o número do BIN da mensagem."""
    bin_parts = message.text.split(None, 1)
    if len(bin_parts) < 2 or len(bin_parts[1]) < 6:
        return None
    return bin_parts[1]


async def fetch_bin_info(bin_number):
    """Busca informações do BIN usando a API e retorna uma mensagem formatada."""
    LOGGER(__name__).info(f"Buscando informações do BIN: {bin_number}")
    resp = await api.bininfo(bin=bin_number)
    return (
        f"<b>💠 Detalhes Completos do BIN:</b>\n"
        f"<b>🏦 Banco:</b> <tt>{resp.bank}</tt>\n"
        f"<b>💳 Bin:</b> <tt>{resp.bin}</tt>\n"
        f"<b>🏡 País:</b> <tt>{resp.country}</tt>\n"
        f"<b>🇮🇳 Bandeira:</b> <tt>{resp.flag}</tt>\n"
        f"<b>🧿 ISO:</b> <tt>{resp.iso}</tt>\n"
        f"<b>⏳ Nível:</b> <tt>{resp.level}</tt>\n"
        f"<b>🔴 Pré-pago:</b> <tt>{resp.prepaid}</tt>\n"
        f"<b>🆔 Tipo:</b> <tt>{resp.type}</tt>\n"
        f"<b>ℹ️ Fornecedor:</b> <tt>{resp.vendor}</tt>"
    )
