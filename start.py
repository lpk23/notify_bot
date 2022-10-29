import asyncio
import logging
from aiogram import Bot, Dispatcher, types
import json


# Загрузка конфига
def load_settings():
    with open("settings.json", 'r', encoding='UTF8') as f:
        data = json.loads(f)
    return data

settings = load_settings()  # Получение данных из конфига
logging.basicConfig(level=logging.INFO)  # Логирования
bot = Bot(token=settings['api_key'])  # Объект бота
dp = Dispatcher(bot)  # Диспетчер

#Получения id чата
@dp.message_handler(commands=['id'])
async def send_welcome(message: types.Message):
    await message.reply(message.chat.id)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


# Тута запуск :)
if __name__ == '__main__':
    asyncio.run(main())  # Старт
