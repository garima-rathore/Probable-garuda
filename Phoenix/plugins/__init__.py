import datetime
from phoenix import *
from phoenix.config import Config
from phoenix.helpers import *
from phoenix.utils import *
from phoenix.random_strings import *
from phoenix.version import __phoenix__
from telethon import version


PHOENIX_USER = bot.me.first_name
me_izz_shreef = bot.uid
phoenix_mention = f"[{PHOENIX_USER}](tg://user?id={me_izz_shreef})"
phoenix_logo = "./phoenix/resources/pics/poison_logo.jpg"
cjb = "./hellbot/resources/pics/cjb.jpg"
restlo = "./phoenix/resources/pics/rest.jpeg"
shuru = "./phoenix/resources/pics/shuru.jpg"
pl = Config.HANDLER
shl = Config.SUDO_HANDLER
phoenix_ver = __phoenix__
phoenix_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"

START_TIME = datetime.datetime.now()
uptime = f"{str(datetime.datetime.now() - START_TIME).split('.')[0]}"
my_channel = Config.MY_CHANNEL or "shinchan_the_h4ch3r"
my_group = Config.MY_GROUP or "phoenixusersupport"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/shinchan_the_h4ch3r"
phoenix_channel = f"[†hê ρнσєηιχ]({chnl_link})"
grp_link = "https://t.me/phoenixusersupport" 
phoenix_grp = f"[ρнσєηιχ ʙᴏᴛ Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon

# ρнσєηιχ
