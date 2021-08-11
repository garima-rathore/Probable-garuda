import datetime
from hellbot import *
from hellbot.config import Config
from hellbot.helpers import *
from hellbot.utils import *
from hellbot.random_strings import *
from hellbot.version import __hell__
from telethon import version


HELL_USER = bot.me.first_name
me_izz_shreef = bot.uid
hell_mention = f"[{HELL_USER}](tg://user?id={me_izz_shreef})"
hell_logo = "./hellbot/resources/pics/poison_logo.jpg"
cjb = "./hellbot/resources/pics/cjb.jpg"
restlo = "./hellbot/resources/pics/rest.jpeg"
shuru = "./hellbot/resources/pics/shuru.jpg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
hell_ver = __hell__
tel_ver = version.__version__

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
my_group = Config.MY_GROUP or "shinchan_the_hacker"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/shinchan_the_h4ch3r"
hell_channel = f"[†hê ρøıƨøп ʙᴏᴛ]({chnl_link})"
grp_link = "https://t.me/shinchan_the_hacker"
hell_grp = f"[ρøıƨøп ʙᴏᴛ Group]({grp_link})"

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

# hellbot