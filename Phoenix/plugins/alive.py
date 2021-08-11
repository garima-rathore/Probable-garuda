from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

hell_pic = Config.ALIVE_PIC or "https://telegra.ph/file/0d043036c5c309404c734.mp4"
alive_c = f"""  🔺 ╔═══╗                   ╔═══╗ 🔺  
╔══🔥🔥  ρøıƨøп ʙᴏᴛ  🔥🔥══╗
 🔻╚═══╝                   ╚═══╝ 🔻

 ┏━━━━━━━━━━━━━━━━
 ┣ ✪ 🅼**ᴀꜱᴛᴇʀ** ✪
 ┣
 ┣『 {hell_mention} 』
 ┣
 ┗━━━━━━━━━━━━━━━━  
┏━━━━━━━━━━━━━━━━
┣ ➤ **𝐓ᴇʟᴇᴛʜᴏɴ 𝐕ᴇʀꜱɪᴏɴ** 
┣      ┗ ⌜{tel_ver}⌟
┣━━━━━━━━━━━━━━━━
┣ ➤ **𝐏ᴏɪꜱᴏɴ 𝐕ᴇʀꜱɪᴏɴ**
┣      ┗ ⌜{hell_ver}⌟
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

@bot.on(hell_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(hell):
    if hell.fwd_from:
        return
    await hell.get_chat()
    await hell.delete()
    await bot.send_file(hell.chat_id, hell_pic, caption=alive_c)
    await hell.delete()

msg = f"""
**⚡  ρøıƨøп ʙᴏᴛ Øp ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**Telethon :**  `{tel_ver}`
** ☠ρøıƨøп ʙᴏᴛ☠ :**  **{hell_ver}**
**Uptime   :**  `{uptime}`
**Abuse    :**  **{abuse_m}**
**Sudo      :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME

@bot.on(hell_cmd(pattern="poison$"))
@bot.on(sudo_cmd(pattern="poison$", allow_sudo=True))
async def hell_a(event):
    try:
        hell = await bot.inline_query(botname, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == me_izz_shreef:   #Maybe it may result in an error 😂  ©TheTitansNetwork
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "poison", None, "Shows Inline Alive Menu with more details." # ©TheTitansNetwork 2021-23
).add_warning(
  "✅ Harmless Module"
).add()
