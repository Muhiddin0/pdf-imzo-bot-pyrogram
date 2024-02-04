import logging
from pyrogram import Client

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from dotenv import load_dotenv
import os
load_dotenv()


API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
API_TOKEN = os.getenv("BOT_TOKEN")
MEDIA_PATH = 'medias/'

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
app = Client('./sessions/session', api_hash=API_HASH, api_id=API_ID)