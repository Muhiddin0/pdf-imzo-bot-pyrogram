from loader import app, MEDIA_PATH
from pyrogram import filters, Client
from pyrogram.types import Message

import requests

# Utils
from utils import buttons, texts

import os

async def progress_callback(current, total, chat_id, message_id, doc_index):
  percent = (current / total) * 100
  print(percent)

  await app.edit_message_text(
    text=f"{doc_index}-fayil {percent:.2f}% yuklandi",
    message_id=message_id,
    chat_id=chat_id
  )

# Define a handler for the /start command
@app.on_message(filters.text & filters.regex(r"(?i)✅ Tugatish"))
async def start_command_handler(client:Client, message: Message):
  
  chat_id = message.from_user.id
  message_id = message.id

  progres_message = await client.send_message(
    text=texts.UPLOADIN_START,
    chat_id=chat_id,
  )
  

  poster_uid = MEDIA_PATH + f"{chat_id}_{message_id}.png"

  r = requests.get(files['poster'])
  with open(poster_uid, "wb") as poster:
    poster.write(r.content)
  
  for index, item in enumerate(files['docs']):

    file_url = item['doc']
    file_name = item['file_name']
    
    r = requests.get(file_url)
    file_uid = MEDIA_PATH + f"{chat_id}_{message_id}_{index}.pdf"
    
    doc_index = index + 1
    with open(file_uid, "wb") as pdf:
      pdf.write(r.content)

    document_message = await client.send_document(
      document=file_uid,
      thumb=poster_uid,
      chat_id=chat_id,
      file_name=file_name,
      progress=progress_callback,
      progress_args=(chat_id, progres_message.id, doc_index)
    )

    await client.forward_messages(
      chat_id="@jzjdksksn",
      from_chat_id="@anipechatchiuzbot",
      message_ids=document_message.id,
    )
    
    os.remove(file_uid)
  os.remove(poster_uid)
  

  user_states[message.chat.id] = START
  
  await client.send_message(chat_id=chat_id, text=texts.MENU, reply_markup=buttons.MENU)