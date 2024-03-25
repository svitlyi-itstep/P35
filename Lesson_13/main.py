import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7026397921:AAFpAYDlvhpYlcpBSxOVst4oDv1AueMU7Q4")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer(text='/help – отримати довідку за командами')
    # await message.reply(text='Help command')
    # await bot.send_message(chat_id=message.chat.id, text='Help command')

'''
    Зробити команду /roll, яка буде виводити випадкове число від 1 до 100.
    Наприклад:
    Випадкове число від 1 до 100: 67
'''
@dp.message()
async def message(message: types.Message):
    await message.answer(message.text)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())