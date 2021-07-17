import requests
from pyrogram import Client as Bot

from Musical.config import API_HASH
from Musical.config import API_ID
from Musical.config import BG_IMAGE
from Musical.config import BOT_TOKEN
from Musical.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Musical.modules"),
)

bot.start()
run()
