from loader import app
from pyrogram import filters
from datas import userdata

# Utils
from utils import buttons, texts

# Define a handler for the /start command
@app.on_message(filters.command("start"),  )
async def start_command_handler(client, message):
    chat_id = message.chat.id
    userdata[chat_id] = False

    # Send the initial message
    await message.reply_text(texts.MENU, reply_markup=buttons.MENU)
