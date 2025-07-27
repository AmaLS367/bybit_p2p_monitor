import requests
from dotenv import load_dotenv
from config import BOT_TOKEN, CHAT_ID

load_dotenv() 

BOT_TOKEN = BOT_TOKEN
CHAT_ID = CHAT_ID

def send_telegram_message(message: str) -> bool:
    if not BOT_TOKEN or not CHAT_ID:
        print("BOT_TOKEN или CHAT_ID не найдены в .env")
        return False

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, data=payload, timeout=10)
        if response.status_code == 200:
            print("Уведомление отправлено в Telegram")
            return True
        else:
            print(f"Ошибка отправки: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Telegram error: {e}")
        return False
