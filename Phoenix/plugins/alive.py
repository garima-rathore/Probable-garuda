from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

phoenix_pic = Config.ALIVE_PIC or "https://telegra.ph/file/337b449d72c39b88f3167.jpg"
alive_c = f"""  πΊ βββββ                   βββββ πΊ  
βββπ₯π₯  π»ππππππ π­ππ  π₯π₯βββ
 π»βββββ                   βββββ π»

 βββββββββββββββββ
 β£ βͺ πΌ**α΄κ±α΄α΄Κ** βͺ
 β£
 β£γ {phoenix_mention} γ
 β£
 βββββββββββββββββ  
βββββββββββββββββ
β£ β€ **πα΄Κα΄α΄Κα΄Ι΄ πα΄Κκ±Ιͺα΄Ι΄** 
β£      β β{tel_ver}β
β£ββββββββββββββββ
β£ β€ **ΟΠ½ΟΡΞ·ΞΉΟ πα΄Κκ±Ιͺα΄Ι΄**
β£      β β{phoenix_ver}β
β£ββββββββββββββββ
β£ β€ **πα΄α΄α΄** 
β£      β β{is_sudo}β
β£ββββββββββββββββ
β£ β€ **πΚα΄Ι΄Ι΄α΄Κ** 
β£      β  β [α΄α΄ΙͺΙ΄](https://t.me/shinchan_the_h4ch3r) β
β£ββββββββββββββββ
β£ β€ **[πΚα΄α΄α΄α΄Κ]**(Https://t.me/me_izz_shreef)
βββββββββββββββββ
"""


# MADE BY TECHNO PRO ( @DARK_DEVIL_OP ) π₯Ίπ₯Ί

# @me_izz_shreef is Piro π₯Ίπ

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
**β‘  α΄Κα΄α΄Ι΄Ιͺx  Κα΄α΄ α΄‘α΄Κα΄ΙͺΙ΄Ι’ κ±α΄α΄α΄α΄κ±κ±κ°α΄ΚΚΚ
 β‘**
{Config.ALIVE_MSG}
**π π±ππ ππππππ π**
**Telethon :**  `{tel_ver}`
** β ΟΠ½ΟΡΞ·ΞΉΟ β  :**  **{phoenix_ver}**
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
        if event.sender_id == me_izz_shreef:   #Maybe it may result in an error π  
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "phoenix", None, "Shows Inline Alive Menu with more details." 
).add_warning(
  "β Harmless Module"
).add()
