from loader import app
from pyrogram import filters, Client
from pyrogram.types import Message


# States
from datas import userdata

# Utils
from utils import buttons, texts

# Define a handler for the /start command
@app.on_message(filters.text & filters.regex(r"(?i)📄 PDF"))
async def start_command_handler(client:Client, message: Message):
  chat_id =message.chat.id
  userdata[chat_id] = False
  
  await client.send_message(chat_id=chat_id, text=texts.SET_PDF, reply_markup=buttons.CANCEL)