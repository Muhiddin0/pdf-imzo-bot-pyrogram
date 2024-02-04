from loader import app
from pyrogram import filters, Client
from pyrogram.types import Message

# Utils
from utils import buttons, texts, files

# Define a handler for the /start command
@app.on_message(filters.document)
async def start_command_handler(client:Client, message: Message):
  chat_id = message.from_user.id
  document_id = message.document.file_id
  file_name = message.document.file_name
  # state = user_states.get(chat_id, INITIAL_STATE)

  doc_url = files.getFile(document_id)

  await client.send_message(chat_id=chat_id, text=texts.DOC_LIMIT.format(1),  reply_markup=buttons.CANCEL_OR_FINISH)