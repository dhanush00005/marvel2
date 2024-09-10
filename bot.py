# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import random, asyncio

from pyrogram.types import Chat, Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

if cfg.SESSION_STRING:
    user = Client(
        "person",
        api_id=cfg.API_ID,
        api_hash=cfg.API_HASH,
        session_string=cfg.SESSION_STRING
    ).start()
else:
    user = None

gif = [
    'https://te.legra.ph/file/a1b3d4a7b5fce249902f7.mp4',
    'https://te.legra.ph/file/0c855143a4039108df602.mp4',
    'https://te.legra.ph/file/d7f3f18a92e6f7add8fcd.mp4',
    'https://te.legra.ph/file/9e334112ee3a4000c4164.mp4',
    'https://te.legra.ph/file/652fc39ae6295272699c6.mp4',
    'https://te.legra.ph/file/702ca8761c3fd9c1b91e8.mp4',
    'https://te.legra.ph/file/a1b3d4a7b5fce249902f7.mp4',
    'https://te.legra.ph/file/d7f3f18a92e6f7add8fcd.mp4',
    'https://te.legra.ph/file/0c855143a4039108df602.mp4',
    'https://te.legra.ph/file/9e334112ee3a4000c4164.mp4',
    'https://te.legra.ph/file/702ca8761c3fd9c1b91e8.mp4'
]


async def send_approval_message(user_id: int, user_mention: str, chat: Chat, client: Client):
    try:
        try:
            await app.send_video(user_id,
                                random.choice(gif),
                                f"**Hello {user_mention}!\nWelcome To {chat.title}\n\n__Powerd By : @VJ_Botz __**")
        except:
            pass
        await client.approve_chat_join_request(chat.id, user_id)
        add_group(chat.id)
        add_user(user_id)
        return True
    except FloodWait as e:
        await asyncio.sleep(e.value + 1)
        await send_approval_message(user_id, user_mention, chat, client)
    except Exception as e:
        print(str(e))


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(client, m : Message):
    await send_approval_message(m.from_user.id, m.from_user.mention, m.chat, client)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


@app.on_message(filters.command("start"))
async def op(_, m :Message):
    if m.chat.type == enums.ChatType.PRIVATE:
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🗯 Channel", url="https://t.me/vj_botz"),
                    InlineKeyboardButton("💬 Support", url="https://t.me/vj_bot_disscussion")
                ],[
                    InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/vjmasterblastbot?startgroup")
                ]
            ]
        )
        add_user(m.from_user.id)
        await m.reply_photo("https://graph.org/file/d57d6f83abb6b8d0efb02.jpg", caption="**🦊 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n__Powerd By : @VJ_Botz __**".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)

    elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
        keyboar = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="https://t.me/vjmasterblastbot?startgroup")
                ]
            ]
        )
        add_group(m.chat.id)
        await m.reply_text("**🦊 Hello {}!\nwrite me private for more details**".format(m.from_user.first_name), reply_markup=keyboar)
    print(m.from_user.first_name +" Is started Your Bot!")
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command(["run", "approve"], [".", "/"]))
async def approve_all(_, message: Message):
    if not user:
        await message.reply_text( "**Session stirng required, fill in config!**", True)
        return

    count = 0

    async for joiner in user.get_chat_join_requests(message.chat.id):
        if await send_approval_message(joiner.user.id, joiner.user.mention, message.chat, user):
            count += 1

    if not count:
        await message.reply_text("**No pending join requests**", True)
        return

    msg = await message.reply_text("**Task Completed** ✓ **Approved Pending All Join Request**", True)
    await asyncio.sleep(5)
    await asyncio.gather(message.delete(), msg.delete())

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    if cb.message.chat.type == enums.ChatType.PRIVATE:
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🗯 Channel", url="https://t.me/VJ_Botz"),
                    InlineKeyboardButton("💬 Support", url="https://t.me/vj_bot_disscussion")
                ],[
                    InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/vjmasterblastbot?startgroup")
                ]
            ]
        )
        add_user(cb.from_user.id)
        await cb.message.edit("**🦊 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n__Powerd By : @VJ_Botz __**".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard, disable_web_page_preview=True)
    print(cb.from_user.first_name +" Is started Your Bot!")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

print("I'm Alive Now!")
app.run()
