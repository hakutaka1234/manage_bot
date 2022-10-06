# AI Chat (C) 2020-2021 by @InukaAsith

import emoji
import re
import aiohttp
from googletrans import Translator as google_translator
from pyrogram import filters
from aiohttp import ClientSession
from HakutakaRobot import BOT_USERNAME as bu
from HakutakaRobot import BOT_ID, pbot, arq
from HakutakaRobot.qq_plugins.chatbot import add_chat, get_session, remove_chat
from HakutakaRobot.utils.pluginhelper import admins_only, edit_or_reply

url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

translator = google_translator()


async def lunaQuery(query: str, user_id: int):
    luna = await arq.luna(query, user_id)
    return luna.result


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


async def fetch(url):
    try:
        async with aiohttp.Timeout(10.0):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    try:
                        data = await resp.json()
                    except:
                        data = await resp.text()
            return data
    except:
        print("AI response Timeout")
        return


ewe_chats = []
en_chats = []


@pbot.on_message(filters.command(["chatbot", f"chatbot@{bu}"]) & ~filters.edited & ~filters.bot & ~filters.private)
@admins_only
async def hmm(_, message):
    global ewe_chats
    if len(message.command) != 2:
        await message.reply_text("I only recognize /chatbot on and /chatbot off only")
        message.continue_propagation()
    status = message.text.split(None, 1)[1]
    chat_id = message.chat.id
    if status == "ON" or status == "on" or status == "On":
        lel = await edit_or_reply(message, "`Processing...`")
        lol = add_chat(int(message.chat.id))
        if not lol:
            await lel.edit("haku AI Already Activated In This Chat")
            return
        await lel.edit(f"haku AI Actived by {message.from_user.mention()} for users in {message.chat.title}")

    elif status == "OFF" or status == "off" or status == "Off":
        lel = await edit_or_reply(message, "`Processing...`")
        Escobar = remove_chat(int(message.chat.id))
        if not Escobar:
            await lel.edit("haku AI Was Not Activated In This Chat")
            return
        await lel.edit(f"haku AI Deactivated by {message.from_user.mention()} for users in {message.chat.title}")

    elif status == "EN" or status == "en" or status == "english":
        if not chat_id in en_chats:
            en_chats.append(chat_id)
            await message.reply_text(f"English AI chat Enabled by {message.from_user.mention()}")
            return
        await message.reply_text(f"English AI Chat Disabled by {message.from_user.mention()}")
        message.continue_propagation()
    else:
        await message.reply_text("I only recognize `/chatbot on` and `chatbot off` only")


@pbot.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited
    & ~filters.via_bot
    & ~filters.forwarded,
    group=2,
)
async def hmm(client, message):
    if not get_session(int(message.chat.id)):
        return
    if not message.reply_to_message:
        return
    try:
        senderr = message.reply_to_message.from_user.id
    except:
        return
    if senderr != BOT_ID:
        return
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        test = msg
        test = test.replace("haku", "only")
        test = test.replace("haku", "only")
        test = test.replace("My god is @gemini_hakutaka", "I'm a Goodboy")
        test = test.replace("18", "9")
        test = test.replace("@gemini_hakutaka is my husband.", "I'm single.")
        test = test.replace("My husband is @Hakuyvbss", "I'm single.")
        test = test.replace("@hakuSupport", "hakubot.ai")
        test = test.replace("I live in @hakuSupport.", "I live in San Francisco, California.")
        test = test.replace("I was created by @Hakuyvbss", "I made myself")
        test = test.replace(
            "Hello there I am haku...nice to meet u",
            "Hi, my friend! Do you want me to tell you a joke?")
        test = test.replace("@Hakuyvbss is my owner", "Have the control right.")
        test = test.replace(
            "Hi, My name is haku Nice to meet you.",
            "Hi, my friend, what can I do for you today?")
        response = await lunaQuery(
            test, message.from_user.id if message.from_user else 0
        )
        response = response.replace("haku", "haku")
        response = response.replace("Haku", "haku")
        response = response.replace("Luna", "haku")
        response = response.replace("luna", "haku")
        response = response.replace("I'm a Goodboy", "My god is @Hakuyvbss")
        response = response.replace("9", "18")
        response = response.replace("I'm married to my job.", "I'm married with @Hakuyvbss")
        response = response.replace("I'm single.", "My husband is @Hakuyvbss")
        response = response.replace("hakubot.ai", "@hakuSupport")
        response = response.replace("I live in San Francisco, California.", "I live in @hakuSupport.")
        response = response.replace("I made myself", "I was Created by @Hakuyvbss")
        response = response.replace(
                "Hi, my friend! Do you want me to tell you a joke?",
                "Hello there I am haku...nice to meet u")
        response = response.replace("Have the control right.", "@Hakuyvbss is my owner.")
        response = response.replace(
                "Hi, my friend, what can I do for you today?",
                "Hi, My name is haku Nice to meet you")

        pro = response
        try:
            await pbot.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return

    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if (
            [(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
        ):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            # print (rm)
        try:
            lan = translator.detect(rm)
            lan = lan.lang
        except:
            return
        test = rm
        if not "en" in lan and not lan == "":
            try:
                test = translator.translate(test, dest="en")
                test = test.text
            except:
                return
        # test = emoji.demojize(test.strip())

        test = test.replace("haku", "Haku")
        test = test.replace("haku", "Haku")
        test = test.replace("My god is @Hakuyvbss", "I'm a Goodboy")
        test = test.replace("18", "9")
        test = test.replace("@Hakuyvbss is my husband.", "I'm single.")
        test = test.replace("@hakuSupport", "hakubot.ai")
        test = test.replace("I live in @hakuSupport.", "I live in San Francisco, California")
        test = test.replace("I was created by @Hakuyvbss", "I made myself")
        test = test.replace(
            "Hello there I am haku...nice to meet u",
            "Hi, my friend! Do you want me to tell you a joke?")
        test = test.replace("@Hakuyvbss is my owner", "Have the control right.")
        test = test.replace(
            "Hi, My name is haku Nice to meet you.",
            "Hi, my friend, what can I do for you today?")
        response = await lunaQuery(
            test, message.from_user.id if message.from_user else 0
        )
        response = response.replace("Haku", "haku")
        response = response.replace("Haku", "haku")
        response = response.replace("Luna", "haku")
        response = response.replace("luna", "haku")
        response = response.replace("I'm a Goodboy", "My god is @Hakuyvbss")
        response = response.replace("9", "18")
        response = response.replace("I'm married to my job.", "I'm married with @Hakuyvbss")
        response = response.replace("I'm single.", "My husband is @Hakuyvbss")
        response = response.replace("hakubot.ai", "@hakuSupport")
        response = response.replace("I live in San Francisco, California.", "I live in @hakuSupport.")
        response = response.replace("I made myself", "I was Created by @Hakuyvbss")
        response = response.replace(
                "Hi, my friend! Do you want me to tell you a joke?",
                "Hello there I am haku...nice to meet u")
        response = response.replace("Have the control right.", "@Hakuyvbss is my owner.")
        response = response.replace(
                "Hi, my friend, what can I do for you today?",
                "Hi, My name is haku Nice to meet you")
        pro = response
        if not "en" in lan and not lan == "":
            try:
                pro = translator.translate(pro, dest=lan)
                pro = pro.text
            except:
                return
        try:
            await pbot.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return


@pbot.on_message(filters.text & filters.private & ~filters.edited & filters.reply & ~filters.bot)
async def inuka(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
        lan = lan.lang
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, dest="en")
            test = test.text
        except:
            return
    test = test.replace("haku", "Haku")
    test = test.replace("haku", "Haku")
    test = test.replace("My god is @Hakuyvbss", "I'm a Goodboy")
    test = test.replace("18", "9")
    test = test.replace("@Hakuyvbss is my husband.", "I'm single.")
    test = test.replace("@hakuSupport", "hakubot.ai")
    test = test.replace("I live in @hakuSupport.", "I live in San Francisco, California.")
    test = test.replace("I was created by @Hakuyvbss", "I made myself")
    test = test.replace(
        "Hello there I am haku...nice to meet u",
        "Hi, my friend! Do you want me to tell you a joke?")
    test = test.replace("@Hakuyvbss is my owner", "Have the control right.")
    test = test.replace(
        "Hi, My name is haku Nice to meet you.",
        "Hi, my friend, what can I do for you today?")

    response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
    response = response.replace("Haku", "haku")
    response = response.replace("Haku", "haku")
    response = response.replace("Luna", "haku")
    response = response.replace("luna", "haku")
    response = response.replace("I'm a Goodboy", "My god is @Hakuyvbss")
    response = response.replace("9", "18")
    response = response.replace("I'm married to my job.", "I'm married with @Hakuyvbss")
    response = response.replace("I'm single.", "My husband is @Hakuyvbss")
    response = response.replace("hakubot.ai", "@hakuSupport")
    response = response.replace("I live in San Francisco, California.", "I live in @hakuSupport")
    response = response.replace("I made myself", "I was Created by @Hakuyvbss")
    response = response.replace(
            "Hi, my friend! Do you want me to tell you a joke?",
            "Hello there I am haku...nice to meet u")
    response = response.replace("Have the control right.", "@Hakuyvbss is my owner.")
    response = response.replace(
            "Hi, my friend, what can I do for you today?",
            "Hi, My name is haku Nice to meet you")

    pro = response
    if not "en" in lan and not lan == "":
        pro = translator.translate(pro, dest=lan)
        pro = pro.text
    try:
        await pbot.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError:
        return


@pbot.on_message(filters.regex("haku|haku|robot|haku|Haku") & ~filters.bot & ~filters.via_bot  & ~filters.forwarded & ~filters.reply & ~filters.channel & ~filters.edited)
async def inuka(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
        lan = lan.lang
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, dest="en")
            test = test.text
        except:
            return
    response = response.replace(
            "Hi, my friend, what can I do for you today?",
            "Hi, My name is haku Nice to meet you")

    pro = response
    if not "en" in lan and not lan == "":
        try:
            pro = translator.translate(pro, dest=lan)
            pro = pro.text
        except Exception:
            return
    try:
        await pbot.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError:
        return


__help__ = """
✪ haku AI is the only ai system which can detect & reply upto 200 language's
✪ /chatbot [ON/OFF]: Enables and disables AI Chat mode.
✪ /chatbot EN : Enables English only chatbot.
"""

__mod_name__ = "Chatbot"
