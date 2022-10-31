import json
import random
import time

import telebot


def load_settings():
    with open("settings.json", 'r', encoding='UTF-8') as f:
        data = json.load(f)
    return data
def send_message():
    with open(settings['file'],'r',encoding='UTF-8') as f:
        data=f.read()
    return data

if __name__ == '__main__':
    settings = load_settings()  # Получение данных из конфига
    bot = telebot.TeleBot(settings['api_key'])
    message=send_message()
    for i in range(0,1):
        for a in settings['chat_id']:
            if message!=settings['last_name']:
                m=bot.send_message(a,f"{message}")
                bot.pin_chat_message(a,m.message_id)
                settings['last_name']=message
            else:
                print("Плохо")
    with open('settings.json','w', encoding='UTF-8') as f:
        json.dump(settings,f,indent=4)

