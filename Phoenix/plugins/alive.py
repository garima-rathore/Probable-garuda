from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

phoenix_pic = Config.ALIVE_PIC or "https://telegra.ph/file/337b449d72c39b88f3167.jpg"
alive_c = f"""  🔺 ╔═══╗                   ╔═══╗ 🔺  
╔══🔥🔥  𝕻𝖍𝖔𝖊𝖓𝖎𝖝 𝕭𝖔𝖙  🔥🔥══╗
 🔻╚═══╝                   ╚═══╝ 🔻

 ┏━━━━━━━━━━━━━━━━
 ┣ ✪ 🅼**ᴀꜱᴛᴇʀ** ✪
 ┣
 ┣『 {phoenix_mention} 』
 ┣
 ┗━━━━━━━━━━━━━━━━  
┏━━━━━━━━━━━━━━━━
┣ ➤ **𝐓ᴇʟᴇᴛʜᴏɴ 𝐕ᴇʀꜱɪᴏɴ** 
┣      ┗ ⌜{tel_ver}⌟
┣━━━━━━━━━━━━━━━━
┣ ➤ **ρнσєηιχ 𝐕ᴇʀꜱɪᴏɴ**
┣      ┗ ⌜{phoenix_ver}⌟
┣━━━━━━━━━━━━━━━━
┣ ➤ **𝐒ᴜᴅᴏ** 
┣      ┗ ⌜{is_sudo}⌟
┣━━━━━━━━━━━━━━━━
┣ ➤ **𝐂ʜᴀɴɴᴇʟ** 
┣      ┗  ⌜ [ᴊᴏɪɴ](https://t.me/shinchan_the_h4ch3r) ⌟
┣━━━━━━━━━━━━━━━━
┣ ➤ **[𝐂ʀᴇᴀᴛᴏʀ]**(Https://t.me/me_izz_shreef)
┗━━━━━━━━━━━━━━━━
"""


# MADE BY TECHNO PRO ( @DARK_DEVIL_OP ) 🥺🥺

# @me_izz_shreef is Piro 🥺😂

#hmm......m

#-------------------------------------------------------------------------------

@bot.on(phoenix_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(phoenix):
    if phoenix.fwd_from:
        return
    await phoenix.get_chat()
    await phoenix.delete()
    await bot.send_file(phoenix.chat_id, phoenix_pic, caption=alive_c)
    await phoenix.delete()

msg = f"""
**⚡  ᴘʜᴏᴇɴɪx  ʙᴏᴛ ᴡᴏʀᴋɪɴɢ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ
 ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**Telethon :**  `{tel_ver}`
** ☠ρнσєηιχ ☠ :**  **{phoenix_ver}**
**Uptime   :**  `{uptime}`
**Abuse    :**  **{abuse_m}**
**Sudo      :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME

@bot.on(phoenix_cmd(pattern="phoenix$"))
@bot.on(sudo_cmd(pattern="phoenix$", allow_sudo=True))
async def phoenix_a(event):
    try:
        phoenix = await bot.inline_query(botname, "alive")
        await phoenix[0].click(event.chat_id)
        if event.sender_id == me_izz_shreef:   #Maybe it may result in an error 😂  
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "phoenix", None, "Shows Inline Alive Menu with more details." 
).add_warning(
  "✅ Harmless Module"
).add()
