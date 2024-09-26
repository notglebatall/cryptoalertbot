import os

from telegram import Bot
from dotenv import load_dotenv

load_dotenv()


def send_alert(data):
    msg = data["msg"]
    if "Buy" in msg:
        msg = msg.replace("Buy signal for", "🟢 Buy signal for")
    elif "Sell" in msg:
        msg = msg.replace("Sell signal for", "🔴 Sell signal for")

    # Достаём название тикера из сообщения
    ticker = msg.split("for ")[1]

    # Заменяем название тикера на гиперссылку
    msg = msg.replace(f"for {ticker}", f"for [{ticker}](https://www.tradingview.com/chart/{ticker}/)")

    tg_bot = Bot(token=os.getenv('BOT_TOKEN'))
    try:
        tg_bot.sendMessage(
            os.getenv('CHANNEL_ID'),
            msg,
            parse_mode="MARKDOWN",
        )
    except KeyError:
        tg_bot.sendMessage(
            os.getenv('CHANNEL_ID'),
            msg,
            parse_mode="MARKDOWN",
        )
    except Exception as e:
        print("[X] Telegram Error:\n>", e)


def send_test_message(text):
    tg_bot = Bot(token=os.getenv('BOT_TOKEN'))
    msg = text
    try:
        tg_bot.sendMessage(
            os.getenv('CHANNEL_ID'),
            msg,
            parse_mode="MARKDOWN",
        )
        print('Message sent')
    except KeyError:
        tg_bot.sendMessage(
            os.getenv('CHANNEL_ID'),
            msg[0],
            parse_mode="MARKDOWN",
        )
    except Exception as e:
        print("[X] Telegram Error:\n>", e)
