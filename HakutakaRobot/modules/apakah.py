import random
from HakutakaRobot.events import register
from HakutakaRobot import telethn

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "YA NDAK TAHU KOK TANYA SAYA",
                 "Pala bapak kau pecah",
                 "Apa iya?",
                 "Tanya aja sama mamak kau tu pler",
                 "Lu tanya gua, terus gua tanya siapa?",
                 "Ebuzed",
                 "Kata Siapa?",
                 "Benar Sekali",
                 "Ngga Bangettt!!!",
                 "ihh Najis Ke GR an Banget si",
                 "Terserah Lu dah",
                 "Iya Si Haku Emang Ganteng"
               
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
