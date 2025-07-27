# 🇷🇺 Тест: проверяет, открывается ли браузер с сохранённым профилем Bybit.
# 🇬🇧 Test: checks if the browser launches correctly with the Bybit user profile.

from playwright.sync_api import sync_playwright

def test_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="user-data-bybit",
            headless=False
        )
        page = browser.new_page()
        page.goto("https://www.bybit.com/ru-RU/fiat/trade/otc/buy/USDT/RUB")
        print("[✅] Браузер успешно открыт.")
        input("Нажми Enter чтобы закрыть...")
        browser.close()

if __name__ == "__main__":
    test_browser()
