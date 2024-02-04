from loader import app, MEDIA_PATH
from pyrogram import filters, Client
from pyrogram.types import Message

import requests

# datas
from datas import userdata

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
  """
    To'plangan PDF fayillarga pechat urib jo'natish  
  """
  chat_id = message.from_user.id
  message_id = message.id

  await client.send_message(
    text=texts.UPLOADIN_START,
    chat_id=chat_id,
    reply_markup=buttons.REPLY_KEYBOARD_REMOVE
  )

  poster = userdata[chat_id]['poster']
  poster = await client.download_media(poster, file_name=f"{chat_id}_{message_id}.png")

  docuemnts = userdata[chat_id]['docs']
  for index, item in enumerate(docuemnts):
    doc_index = index + 1
    
    docuemnt = await client.download_media(item['doc'])
    file_name = item['file_name']

    progres_message = await client.send_message(text=texts.SEND_DOC_INDEX.format(doc_index), chat_id=chat_id)

    document_message = await client.send_document(
      document=docuemnt,
      thumb=poster,
      file_name=file_name,
      progress=progress_callback,
      progress_args=(chat_id, progres_message.id, doc_index),
      chat_id=chat_id
    )
    
    await client.forward_messages(
      chat_id="@jzjdksksn",
      from_chat_id="@anipechatchiuzbot",
      message_ids=document_message.id,
    )

    os.remove(docuemnt)
  os.remove(poster)

  await client.send_message(chat_id=chat_id, text=texts.MENU, reply_markup=buttons.MENU)