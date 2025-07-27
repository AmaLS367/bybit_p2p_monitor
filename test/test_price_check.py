# 🇷🇺 Тест: открывает Bybit, перехватывает JSON-ответ с ценами и выводит минимальный курс.
# 🇬🇧 Test: opens Bybit, intercepts JSON with offers, and prints the lowest price.

from playwright.sync_api import sync_playwright

def extract_price_from_page():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="user-data-bybit",
            headless=False
        )
        page = browser.new_page()
        offers = []

        def handle_response(response):
            if "/x-api/fiat/otc/item/online" in response.url:
                try:
                    json_data = response.json()
                    items = json_data.get("result", {}).get("items", [])
                    offers.extend(items)
                except:
                    pass

        page.on("response", handle_response)
        page.goto("https://www.bybit.com/ru-RU/fiat/trade/otc/buy/USDT/RUB", wait_until="domcontentloaded")
        page.wait_for_timeout(5000)
        browser.close()

        if offers:
            best = min(offers, key=lambda x: float(x["price"]))
            print(f"[✅] Минимальный курс: {best['price']} ₽ от {best['nickName']}")
        else:
            print("[❌] Предложения не найдены.")

if __name__ == "__main__":
    extract_price_from_page()
