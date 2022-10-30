import json
import time

import telebot


def load_settings():
    with open("settings.json", 'r', encoding='UTF8') as f:
        data = json.load(f)
    return data
def send_message():
    with open(settings['file'],'r',encoding='UTF8') as f:
        data=f.read()
    return data

if __name__ == '__main__':
    settings = load_settings()  # Получение данных из конфига
    bot = telebot.TeleBot(settings['api_key'])
    for i in range(0,5):
        for a in settings['chat_id']:
            m=bot.send_message(a,f"Сообщение №{i}")
            bot.pin_chat_message(a,m.message_id)
        time.sleep(10)

