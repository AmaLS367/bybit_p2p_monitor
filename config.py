import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID_RAW = os.getenv("CHAT_ID")

if BOT_TOKEN is None or CHAT_ID_RAW is None:
    raise ValueError("❌ Переменные BOT_TOKEN или CHAT_ID не найдены в .env")

CHAT_ID = int(CHAT_ID_RAW)
