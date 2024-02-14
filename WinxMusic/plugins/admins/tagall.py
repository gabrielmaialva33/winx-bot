import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus, ChatType
from pyrogram.errors import UserNotParticipant

from WinxMusic import app

spam_chats = []

EMOJI = [
    "🦋🦋🦋🦋🦋",
    "🧚🌸🧋🍬🫖",
    "🥀🌷🌹🌺💐",
    "🌸🌿💮🌱🌵",
    "❤️💚💙💜🖤",
    "💓💕💞💗💖",
    "🌸💐🌺🌹🦋",
    "🍔🦪🍛🍲🥗",
    "🍎🍓🍒🍑🌶️",
    "🧋🥤🧋🥛🍷",
    "🍬🍭🧁🎂🍡",
    "🍨🧉🍺☕🍻",
    "🥪🥧🍦🍥🍚",
    "🫖☕🍹🍷🥛",
    "☕🧃🍩🍦🍙",
    "🍁🌾💮🍂🌿",
    "🌨️🌥️⛈️🌩️🌧️",
    "🌷🏵️🌸🌺💐",
    "💮🌼🌻🍀🍁",
    "🧟🦸🦹🧙👸",
    "🧅🍠🥕🌽🥦",
    "🐷🐹🐭🐨🐻‍❄️",
    "🦋🐇🐀🐈🐈‍⬛",
    "🌼🌳🌲🌴🌵",
    "🥩🍋🍐🍈🍇",
    "🍴🍽️🔪🍶🥃",
    "🕌🏰🏩⛩️🏩",
    "🎉🎊🎈🎂🎀",
    "🪴🌵🌴🌳🌲",
    "🎄🎋🎍🎑🎎",
    "🦅🦜🕊️🦤🦢",
    "🦤🦩🦚🦃🦆",
    "🐬🦭🦈🐋🐳",
    "🐔🐟🐠🐡🦐",
    "🦩🦀🦑🐙🦪",
    "🐦🦂🕷️🕸️🐚",
    "🥪🍰🥧🍨🍨",
    " 🥬🍉🧁🧇",
]

TAGMES = [
    " **Ei, bebê, como você está?🤗🥱** ",
    " **Oi, só entre online, vamos lá😊** ",
    " **Vamos conversar um pouco😃** ",
    " **Você comeu..??🥲** ",
    " **Como estão todos em casa?🥺** ",
    " **Sabe, estava sentindo muito sua falta🤭** ",
    " **Oi, como você está..??🤨** ",
    " **Vou ajustar as configurações também..??🙂** ",
    " **Qual é o seu nome..??🥲** ",
    " **Você tomou café da manhã..??😋** ",
    " **Me sequestre para o seu grupo😍** ",
    " **Seu parceiro está te procurando, venha online logo😅😅** ",
    " **Vamos ser amigos..??🤔** ",
    " **Você foi dormir..??🙄🙄** ",
    " **Toque uma música, por favor😕** ",
    " **De onde você é..??🙃** ",
    " **Olá, Namaste😛** ",
    " **Oi, bebê, como você está..?🤔** ",
    " **Você sabe quem é meu dono.?** ",
    " **Vamos jogar algo.🤗** ",
    " **E aí, como você está, bebê?😇** ",
    " **O que sua mãe está fazendo?🤭** ",
    " **Você não vai falar comigo?🥺🥺** ",
    " **Oi, louco, vem online😶** ",
    " **Hoje é feriado ou tem aula..??🤔** ",
    " **Oi, bom dia😜** ",
    " **Escute, tenho um trabalho para você🙂** ",
    " **Toque uma música, vai😪** ",
    " **Prazer em te conhecer☺** ",
    " **Oi🙊** ",
    " **Terminou de estudar??😺** ",
    " **Fale alguma coisa, vai🥲** ",
    " **Quem é Sonali..??😅** ",
    " **Posso ter uma foto sua..??😅** ",
    " **Sua mãe chegou, né😆😆😆** ",
    " **E aí, como está a tia?😉** ",
    " **Eu te amo🙈🙈🙈** ",
    " **Você me ama..??👀** ",
    " **Quando você vai colocar o Rakhi..??🙉** ",
    " **Posso ouvir uma música..??😹** ",
    " **Venha online, estou ouvindo músicas😻** ",
    " **Você usa Instagram..??🙃** ",
    " **Me dê seu número do WhatsApp..??😕** ",
    " **De quem você gosta de ouvir música..??🙃** ",
    " **Você terminou todo o seu trabalho..??🙃** ",
    " **De onde você é?😊** ",
    " **Escute, por favor🧐** ",
    " **Você fará um favor para mim..??** ",
    " **Não fale comigo nunca mais depois de hoje😠** ",
    " **Como estão mamãe e papai..??❤** ",
    " **O que aconteceu..??👱** ",
    " **Estou com muitas saudades 🤧❣️** ",
    " **Você me esqueceu😏😏** ",
    " **Não quero mentir🤐** ",
    " **Não me dê sermão agora😒** ",
    " **O que aconteceu😮😮** ",
    " **Oi👀** ",
    " **Ter amigos como você faz com que eu me sinta especial 🙈** ",
    " **Hoje estou triste ☹️** ",
    " **Fale comigo, por favor 🥺🥺** ",
    " **O que você está fazendo?👀** ",
    " **Como você está? 🙂** ",
    " **De onde você é?🤔** ",
    " **Vamos conversar..??🥺** ",
    " **Eu sou inocente, tá🥺🥺** ",
    " **Você se divertiu ontem, né🤭😅** ",
    " **Por que você não fala no grupo?😕** ",
    " **Você está em um relacionamento..??👀** ",
    " **Por que você fica tão quieto?😼** ",
    " **Você gosta de cantar..??😸** ",
    " **Vamos sair para passear..??🙈** ",
    " **Fique feliz ✌️🤞** ",
    " **Podemos ser amigos...??🥰** ",
    " **Por que você não está falando..??🥺🥺** ",
    " **Adicione alguns membros 🥲** ",
    " **Solteiro ou em um relacionamento? 😉** ",
    " **Vamos para a festa😋🥳** ",
    " **Ei, você🧐** ",
    " **Você me esqueceu, né🥺** ",
    " **Venha aqui:-[@cinewinx] Vamos nos divertir 🤭🤭** ",
    " **Vamos jogar verdade ou desafio..?? 😊** ",
    " **Hoje mamãe brigou comigo🥺🥺** ",
    " **Entre no grupo🤗** ",
    " **Um coração é apenas um coração😗😗** ",
    " **Onde estão seus amigos?🥺** ",
    " **Meu dono fofo{@mrootx}🥰** ",
    " **Onde você se escondeu, querido?😜** ",
    " **Boa noite, já está tarde🥰** ",
]

VC_TAG = [
    "**Ei, venha para o VC, por favor🥲**",
    "**Entre no VC rápido, é importante😬**",
    "**Venha para o VC rápido, bebê🏓**",
    "**Bebê, você também, venha para o VC🥰**",
    "**Ei, engraçadinho, vem pro VC🤨**",
    "**Ouça, entre no VC🤣**",
    "**Venha pro VC uma vez😁**",
    "**O VC está pronto para o jogo⚽**",
    "**Entre no VC ou vai se arrepender🥺**",
    "**Desculpa, bebê, por favor, venha pro VC😥**",
    "**Estar no VC mostra algo🙄**",
    "**No VC, me diga se a música está tocando?🤔**",
    "**Entrar no VC, o que custa? Espera um pouco mais🙂**",
]


@app.on_message(filters.command(["tagall"], prefixes=["/", "@", ".", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("<code>𝐄𝐬𝐭𝐞 𝐜𝐨𝐦𝐚𝐧𝐝𝐨 𝐬𝐨́ 𝐟𝐮𝐧𝐜𝐢𝐨𝐧𝐚 𝐞𝐦 𝐠𝐫𝐮𝐩𝐨𝐬.</code>")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ):
            is_admin = True
    if not is_admin:
        return await message.reply(
            "𝐕𝐨𝐜𝐞̂ 𝐧𝐚̃𝐨 𝐞́ 𝐚𝐝𝐦𝐢𝐧, 𝐛𝐞𝐛𝐞̂, 𝐚𝐩𝐞𝐧𝐚𝐬 𝐚𝐝𝐦𝐢𝐧𝐬 𝐩𝐨𝐝𝐞𝐦 𝐦𝐚𝐫𝐜𝐚𝐫 𝐦𝐞𝐦𝐛𝐫𝐨𝐬."
        )

    if message.reply_to_message and message.text:
        return await message.reply(
            "/tagall 𝐁𝐨𝐦 𝐝𝐢𝐚 👈 𝐃𝐢𝐠𝐢𝐭𝐞 𝐚𝐬𝐬𝐢𝐦 / 𝐑𝐞𝐬𝐩𝐨𝐧𝐝𝐚 𝐪𝐮𝐚𝐥𝐪𝐮𝐞𝐫 𝐦𝐞𝐧𝐬𝐚𝐠𝐞𝐦 𝐩𝐫𝐨́𝐱𝐢𝐦𝐚 𝐯𝐞𝐳 𝐩𝐚𝐫𝐚 𝐦𝐚𝐫𝐜𝐚𝐜̧𝐚̃𝐨..."
        )
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply(
                "/tagall 𝐁𝐨𝐦 𝐝𝐢𝐚 👈 𝐃𝐢𝐠𝐢𝐭𝐞 𝐚𝐬𝐬𝐢𝐦 / 𝐑𝐞𝐬𝐩𝐨𝐧𝐝𝐚 𝐪𝐮𝐚𝐥𝐪𝐮𝐞𝐫 𝐦𝐞𝐧𝐬𝐚𝐠𝐞𝐦 𝐩𝐫𝐨́𝐱𝐢𝐦𝐚 𝐯𝐞𝐳 𝐩𝐚𝐫𝐚 𝐦𝐚𝐫𝐜𝐚𝐜̧𝐚̃𝐨..."
            )
    else:
        return await message.reply(
            "/tagall 𝐁𝐨𝐦 𝐝𝐢𝐚 👈 𝐃𝐢𝐠𝐢𝐭𝐞 𝐚𝐬𝐬𝐢𝐦 / 𝐑𝐞𝐬𝐩𝐨𝐧𝐝𝐚 𝐪𝐮𝐚𝐥𝐪𝐮𝐞𝐫 𝐦𝐞𝐧𝐬𝐚𝐠𝐞𝐦 𝐩𝐫𝐨́𝐱𝐢𝐦𝐚 𝐯𝐞𝐳 𝐩𝐚𝐫𝐚 𝐦𝐚𝐫𝐜𝐚𝐜̧𝐚̃𝐨..."
        )
    if chat_id in spam_chats:
        return await message.reply(
            "𝐏𝐨𝐫 𝐟𝐚𝐯𝐨𝐫, 𝐩𝐚𝐫𝐞 𝐨 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐨 𝐝𝐞 𝐦𝐞𝐧𝐜̧𝐚̃𝐨 𝐩𝐫𝐢𝐦𝐞𝐢𝐫𝐨 𝐮𝐬𝐚𝐧𝐝𝐨 /tagalloff , /stopvctag ..."
        )
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}\n\n|| ➥ ᴅᴇ𝐬𝐚𝐭𝐢𝐯𝐚𝐫 𝐚𝐬 𝐦𝐞𝐧𝐜̧𝐨̃𝐞𝐬 𝐜𝐨𝐦 » /stoptagall ||"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["vctag"], prefixes=["/", ".", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐄𝐬𝐭𝐞 𝐜𝐨𝐦𝐚𝐧𝐝𝐨 𝐞́ 𝐬𝐨́ 𝐩𝐚𝐫𝐚 𝐠𝐫𝐮𝐩𝐨𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ):
            is_admin = True
    if not is_admin:
        return await message.reply(
            "𝐕𝐨𝐜𝐞̂ 𝐧𝐚̃𝐨 𝐞́ 𝐚𝐝𝐦𝐢𝐧, 𝐛𝐞𝐛𝐞̂, 𝐚𝐩𝐞𝐧𝐚𝐬 𝐚𝐝𝐦𝐢𝐧𝐬 𝐩𝐨𝐝𝐞𝐦 𝐦𝐚𝐫𝐜𝐚𝐫 𝐦𝐞𝐦𝐛𝐫𝐨𝐬."
        )
    if chat_id in spam_chats:
        return await message.reply(
            "𝐏𝐨𝐫 𝐟𝐚𝐯𝐨𝐫, 𝐩𝐫𝐢𝐦𝐞𝐢𝐫𝐨 𝐩𝐚𝐫𝐞 𝐨 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐨 𝐝𝐞 𝐦𝐞𝐧𝐜̧𝐨̃𝐞𝐬 𝐮𝐬𝐚𝐧𝐝𝐨 /tagalloff , /stopvctag ..."
        )
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}\n\n|| ➥ ᴅᴇ𝐬𝐚𝐭𝐢𝐯𝐚𝐫 𝐚𝐬 𝐦𝐞𝐧𝐜̧𝐨̃𝐞𝐬 𝐜𝐨𝐦 » /stopvctag ||"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(
    filters.command(
        [
            "stoptagall",
            "canceltagall",
            "offtagall",
            "tagallstop",
            "stopvctag",
            "tagalloff",
        ]
    )
)
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐀𝐭𝐮𝐚𝐥𝐦𝐞𝐧𝐭𝐞 𝐧𝐚̃𝐨 𝐞𝐬𝐭𝐨𝐮 𝐦𝐚𝐫𝐜𝐚𝐧𝐝𝐨, 𝐛𝐞𝐛𝐞̂.")
    is_admin = False
    try:
        participant = await client.get_chat_member(
            message.chat.id, message.from_user.id
        )
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ):
            is_admin = True
    if not is_admin:
        return await message.reply(
            "𝐕𝐨𝐜𝐞̂ 𝐧𝐚̃𝐨 𝐞́ 𝐚𝐝𝐦𝐢𝐧, 𝐛𝐞𝐛𝐞̂, 𝐚𝐩𝐞𝐧𝐚𝐬 𝐚𝐝𝐦𝐢𝐧𝐬 𝐩𝐨𝐝𝐞𝐦 𝐦𝐚𝐫𝐜𝐚𝐫 𝐦𝐞𝐦𝐛𝐫𝐨𝐬."
        )
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ 𝐏𝐚𝐫𝐚𝐝𝐨..♦")
