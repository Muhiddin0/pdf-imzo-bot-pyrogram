from loader import app
from pyrogram import filters, Client
from pyrogram.types import Message

# Datas
from datas import userdata

# Utils
from utils import buttons, texts, files

# Define a handler for the /start command
@app.on_message(filters.photo)
async def start_command_handler(client:Client, message: Message):
  chat_id = message.from_user.id

  if not userdata: raise ValueError("userda malumotlar bor", userdata)
  poster = message.photo.file_id
  userdata[chat_id] = {
    "poster":poster,
    "docs":[]
  }

  poster_id = message.photo.file_id
  print(poster_id)

  await client.send_message(chat_id=chat_id, text=texts.SET_DOC)