import asyncio
import logging
from aiogram import Bot, Dispatcher, types
import json


# Загрузка конфига
def load_settings():
    with open("settings.json", 'r', encoding='UTF8') as f:
        data = json.loads(f)
    return data


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


# Тута запуск :)
if __name__ == '__main__':
    settings = load_settings()  # Получение данных из конфига
    logging.basicConfig(level=logging.INFO)  # Логирования
    bot = Bot(token=settings['api_key'])  # Объект бота
    dp = Dispatcher(bot)  # Диспетчер
    asyncio.run(main())  # Старт
