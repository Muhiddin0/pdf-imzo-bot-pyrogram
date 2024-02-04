from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
                           ReplyKeyboardMarkup, KeyboardButton, \
                           ReplyKeyboardRemove

REPLY_KEYBOARD_REMOVE = ReplyKeyboardRemove()

MENU = ReplyKeyboardMarkup(
    [
      [
        KeyboardButton("📄 PDF"),
        # KeyboardButton("📹 Video")
      ]
    ], resize_keyboard=True
)

CANCEL = ReplyKeyboardMarkup(
    [
      [KeyboardButton("❌ Cancel"),]
    ], resize_keyboard=True
)

CANCEL_OR_FINISH = ReplyKeyboardMarkup(
    [
      [KeyboardButton("❌ Cancel"),],
      [KeyboardButton("✅ Tugatish"),]
    ], resize_keyboard=True
)
