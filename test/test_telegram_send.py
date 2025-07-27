# 🇷🇺 Тест: отправляет тестовое сообщение в Telegram, чтобы проверить работоспособность бота.
# 🇬🇧 Test: sends a test message to Telegram to verify that the bot works.

from telegram_bot import send_telegram_message

if send_telegram_message("🚀 Тестовое сообщение от Bybit-бота!"):
    print("[✅] Уведомление успешно отправлено.")
else:
    print("[❌] Ошибка при отправке.")
