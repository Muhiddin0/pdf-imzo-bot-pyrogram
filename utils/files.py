import requests

# .env
import dotenv
import os
dotenv.load_dotenv()

def getFile(file_id):
  bot_token = os.getenv("BOT_TOKEN")
  r = requests.get(f'https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}').json()
  print(r)
  return f"https://api.telegram.org/file/bot{bot_token}/{r['result']['file_path']}"