from loader import app
from pyrogram import filters, Client
from pyrogram.types import Message

# States
from states import INITIAL_STATE, PDF, user_states

# Utils
from utils import buttons, texts, files

# Define a handler for the /start command
@app.on_message(filters.photo)
async def start_command_handler(client:Client, message: Message):
  chat_id = message.from_user.id
  state = user_states.get(chat_id, INITIAL_STATE)

  poster_id = message.photo.file_id
  print(poster_id)

  if state == PDF:
    user_states[message.chat.id] = {
      "poster":files.getFile(poster_id),
      'docs':[]
    }
    
    await client.send_message(chat_id=chat_id, text=texts.SET_DOC)