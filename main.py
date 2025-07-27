from playwright.sync_api import sync_playwright
from telegram_bot import send_telegram_message
import time

try:
    THRESHOLD = float(input("🔢 Введите пороговое значение (₽): ").replace(",", "."))
except ValueError:
    print("❌ Неверное значение. Вводите число, например: 71.50")
    exit()

CHECK_INTERVAL = 60  # секунд
URL = "https://www.bybit.com/ru-RU/fiat/trade/otc/buy/USDT/RUB"

def start_browser():
    p = sync_playwright().start()
    browser = p.chromium.launch_persistent_context(
        user_data_dir="user-data-bybit",
        headless=False,
        viewport={"width": 1280, "height": 800},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    )
    page = browser.pages[0] if browser.pages else browser.new_page()
    page.goto(URL, wait_until="domcontentloaded", timeout=30000)
    return page

def check_offer(page, last_sent_id):
    offers = []

    def handle_response(response):
        if "/x-api/fiat/otc/item/online" in response.url and response.request.method == "POST":
            try:
                json_data = response.json()
                print("[DEBUG] Перехвачен ответ от Bybit")
                items = json_data.get("result", {}).get("items", [])
                if items:
                    offers.extend(items)
                    print(f"[DEBUG] Добавлено предложений: {len(items)}")
            except Exception as e:
                print(f"[ERROR] Ошибка парсинга JSON: {e}")

    page.on("response", handle_response)

    page.reload(wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(5000)

    if offers:
        best = min(offers, key=lambda x: float(x.get("price", 999999)))
        if float(best["price"]) < THRESHOLD and best["id"] != last_sent_id:
            message = (
                f"📉 <b>Курс ниже порога!</b>\n"
                f"<code>{best['price']} ₽/USDT</code>\n"
                f"👤 {best['nickName']} (ID {best['accountId']})\n"
                f"🔗 <a href='{URL}'>Открыть</a>"
            )
            send_telegram_message(message)
            return best["id"]
    return last_sent_id

def main():
    print("[INFO] Мониторинг запущен...")
    page = start_browser()
    last_id = None

    while True:
        try:
            last_id = check_offer(page, last_id)
        except Exception as e:
            print(f"[ERROR] {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()

# This code monitors the Bybit OTC market for USDT/RUB offers and sends Telegram notifications
# when the price drops below a specified threshold.
# It uses Playwright to interact with the Bybit website and fetch offer data.
# The script runs indefinitely, checking for new offers at regular intervals.
# Make sure to have the necessary dependencies installed and configured.
# Ensure you have the Telegram bot set up to send messages.
# Adjust the THRESHOLD and CHECK_INTERVAL as needed for your use case.

# Этот скрипт отслеживает рынок P2P Bybit по паре USDT/RUB и отправляет уведомления в Telegram,
# если цена падает ниже заданного порога.
# Используется Playwright для открытия страницы Bybit и перехвата данных о предложениях.
# Скрипт работает бесконечно, проверяя новые предложения через регулярные интервалы.
# Убедитесь, что установлены все зависимости и настроен Telegram-бот.
# При необходимости измените значения THRESHOLD (порог цены) и CHECK_INTERVAL (интервал проверки).

