import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from HakutakaRobot.events import register
from HakutakaRobot import telethn as tbot
from HakutakaRobot import BOT_USERNAME as bu
PHOTO = "https://graph.org/file/a4d8ec008094e0e71cbda.jpg"
@register(pattern="^/alive ?(.*)")
async def awake(event):
  Haku = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm ʜᴀᴋᴜ** \n\n"
  Haku += "㊝ **I'm Working Properly** \n\n"
  Haku += f"㊝ **My Master : [〲༆ʜᴀᴋᴜ ᴀʟɪᴠᴇ ༇〺](https://t.me/HakutakaRobot)** \n\n"
  Haku += f"㊝ **Library Version :** `{telever}` \n\n"
  Haku += f"㊝ **Telethon Version :** `{tlhver}` \n\n"
  Haku += f"㊝ **Pyrogram Version :** `{pyrover}` \n\n"
  Haku += "**Thanks For Adding Me Here**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", f"https://t.me/{bu}?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/alivenotalliance")]]
  await tbot.send_file(event.chat_id, PHOTO=None, caption=Haku,  buttons=BUTTON)
