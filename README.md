# Bybit USDT/RUB Price Monitor

## 🇷🇺 Описание

Этот скрипт отслеживает рынок P2P Bybit по паре **USDT/RUB** и отправляет уведомления в Telegram, когда цена падает ниже заданного порога. Используется Playwright для запуска реального браузера, перехвата сетевых запросов и извлечения нужных данных. Подходит для непрерывного фонового мониторинга.

- 💰 Порог цены задаётся через переменную `THRESHOLD`
- ⏱ Интервал проверок — `CHECK_INTERVAL` (в секундах)
- 🔁 Работает бесконечно, браузер остаётся открытым
- 📨 Уведомления отправляются через Telegram-бота

### Требования

- Python 3.8+
- Установленные зависимости из `requirements.txt`
- Настроенный файл `.env` с токеном и chat_id Telegram

### Установка

```bash
pip install -r requirements.txt
playwright install
````

Создайте `.env` файл:

```
BOT_TOKEN=ваш_токен_бота
CHAT_ID=ваш_чат_id
```

### Запуск

```bash
python main.py
```

---

## 🇬🇧 Description

This script monitors the Bybit P2P market for the **USDT/RUB** pair and sends Telegram notifications when the price drops below a specified threshold. It uses Playwright to launch a real browser, intercept network requests, and extract offer data. Ideal for continuous background monitoring.

* 💰 Price threshold defined in `THRESHOLD`
* ⏱ Check interval defined by `CHECK_INTERVAL` (in seconds)
* 🔁 Runs indefinitely, browser remains open
* 📨 Sends alerts via Telegram bot

### Requirements

* Python 3.8+
* Installed dependencies from `requirements.txt`
* Configured `.env` file with Telegram bot token and chat ID

### Installation

```bash
pip install -r requirements.txt
playwright install
```

Create a `.env` file:

```
BOT_TOKEN=your_bot_token
CHAT_ID=your_chat_id
```

### Run the script

```bash
python main.py
```

---

> Made for automation, trading, and monitoring needs.

```

