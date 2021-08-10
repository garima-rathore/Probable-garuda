import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from phoenix import *
from phoenix.helpers import *
from phoenix.config import Config


# just a small shit for big works
class Loader:
    def __init__(self, func=None, **args):
        self.Var = Var
        bot.add_event_handler(func, events.NewMessage(**args))


# To Check if Admin
async def is_admin(client, chat_id, user_id):
    if not str(chat_id).startswith("-100"):
        return False
    try:
        phoenix = await client(GetParticipantRequest(channel=chat_id, user_id=user_id))
        chat_participant = phoenix.participant
        if isinstance(
            chat_participant, (ChannelParticipantCreator, ChannelParticipantAdmin)
        ):
            return True
    except Exception:
        return False
    else:
        return False
