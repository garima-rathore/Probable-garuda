import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from phoenix import LOGS, bot, tbot
from phoenix.config import Config
from phoenix.utils import load_module
from phoenix.version import __phoenix__ as phoenixver
hl = Config.HANDLER
PHOENIX_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/337b449d72c39b88f3167.jpg"

# let's get the bot ready
async def phoenix_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"PHOENIX_SESSION - {str(e)}")
        sys.exit()


# phoenix userbot  starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 Starting 𝕻𝖍𝖔𝖊𝖓𝖎𝖝 𝕭𝖔𝖙 🔰")
            bot.loop.run_until_complete(phoenix_bot(Config.BOT_USERNAME))
            LOGS.info("🔥 𝕻𝖍𝖔𝖊𝖓𝖎𝖝 𝕭𝖔𝖙 Startup Completed 🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "phoenix/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ Your 𝕻𝖍𝖔𝖊𝖓𝖎𝖝 𝕭𝖔𝖙 Is Now Working ⚡")
LOGS.info(
    "Head to @shinchan_the_h4ch3r for Updates. Also join chat group to get help regarding to 𝕻𝖍𝖔𝖊𝖓𝖎𝖝 𝕭𝖔𝖙."
)

# that's life...
async def phoenix_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                PHOENIX_PIC,
                caption=f"#START \n\nDeployed 𝕻𝖍𝖔𝖊𝖓𝖎𝖝 𝕭𝖔𝖙 Successfully\n\n**𝕻𝖍𝖔𝖊𝖓𝖎𝖝 𝕭𝖔𝖙 - {phoenixver}**\n\nType `{pl}ping` or `{pl}alive` to check! \n\nJoin [𝕻𝖍𝖔𝖊𝖓𝖎𝖝 𝕭𝖔𝖙 Channel](t.me/shinchan_the_h4ch3r) for Updates & [𝕻𝖍𝖔𝖊𝖓𝖎𝖝 𝕭𝖔𝖙 Chat](t.me/phoenixusersupport) for any query regarding 𝕻𝖍𝖔𝖊𝖓𝖎𝖝 𝕭𝖔𝖙",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join Phoenix  Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@shicnah_the_h4ch3r"))
    except BaseException:
        pass

# Why not come here and chat??
    try:
        await bot(JoinChannelRequest("@phoenixusersupport"))
    except BaseException:
        pass


bot.loop.create_task(phoenix_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

#  PHOENIX USERBOT OP
