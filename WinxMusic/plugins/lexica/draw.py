from lexica import Client as ApiClient
from pyrogram import Client, filters
from pyrogram import types as t

from WinxMusic import app
from WinxMusic.helpers.lexica_api import lexica_image_generation
from WinxMusic.helpers.lexica_btn_parser import paginate_models
from WinxMusic.helpers.lexica_miscs import get_text
from config import BANNED_USERS

Database = {}
Models = ApiClient().models["models"]["image"]


@app.on_message(
    filters.command(["draw", "create", "imagine", "dream", "desenhe", "art"])
    & filters.group
    & ~BANNED_USERS
)
async def draw(_: Client, m: t.Message):
    global Database
    prompt = get_text(m)
    if prompt is None:
        return await m.reply_text("🖍️você não me deu um prompt para desenhar!")
    user = m.from_user
    data = {"prompt": prompt, "reply_to_id": m.id}
    Database[user.id] = data
    btns = paginate_models(0, Models, user.id)
    await m.reply_text(
        text=f"<b>💭prompt:</b> <i>{prompt}</i>\n\n<b>🤖Escolha um modelo</b>",
        reply_markup=t.InlineKeyboardMarkup(btns),
    )


@app.on_callback_query(filters.regex(pattern=r"^d.(.*)"))
async def select_model(_: Client, query: t.CallbackQuery):
    global Database
    data = query.data.split(".")
    auth_user = int(data[-1])
    if query.from_user.id != auth_user:
        return await query.answer("No.")
    if len(data) > 3:
        if data[1] == "right":
            next_page = int(data[2])
            await query.edit_message_reply_markup(
                t.InlineKeyboardMarkup(
                    paginate_models(next_page + 1, Models, auth_user)
                )
            )
        elif data[1] == "left":
            curr_page = int(data[2])
            await query.edit_message_reply_markup(
                t.InlineKeyboardMarkup(
                    paginate_models(curr_page - 1, Models, auth_user)
                )
            )
        return
    model_id = int(data[1])
    if model_id == -1:
        del Database[auth_user]
        await query.message.delete()
        return
    await query.edit_message_text("<code>🎨 desenhando...</code>")
    prompt_data = Database.get(auth_user, None)
    if prompt_data is None:
        return await query.edit_message_text(
            "🔴<b> algo deu errado, tente novamente mais tarde</b>"
        )
    img_url = await lexica_image_generation(model_id, prompt_data["prompt"])
    if img_url is None or img_url == 2 or img_url == 1:
        return await query.edit_message_text(
            "🔴<b> algo deu errado, tente novamente mais tarde</b>"
        )
    elif img_url == 69:
        return await query.edit_message_text("🔴<b> NSFW não é permitido aqui</b>")
    images = []
    model_name = [i["name"] for i in Models if i["id"] == model_id]
    for i in img_url:
        images.append(t.InputMediaDocument(i))
    images[-1] = t.InputMediaDocument(
        img_url[-1],
        caption=f"<b>💭prompt:</b> <i>{prompt_data['prompt']}</i>\n<b>🤖modelo:</b> <code>{model_name[0]}</code>",
    )
    await query.message.delete()
    try:
        del Database[auth_user]
    except KeyError:
        pass
    await _.send_media_group(
        chat_id=query.message.chat.id,
        media=images,
        reply_to_message_id=prompt_data["reply_to_id"],
    )
