import telegram
from os import environ

token = environ['TELEGRAM_TOKEN']
chat_id = environ['CHAT_ID']

def telegram_notify(message):
    message = message
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)