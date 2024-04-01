import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
import random

from aiogram.fsm.context import FSMContext
from states import SumStates

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7026397921:AAFpAYDlvhpYlcpBSxOVst4oDv1AueMU7Q4")
dp = Dispatcher()

# === COMMAND SUM ===
@dp.message(Command("sum"))
async def cmd_sum(message: types.Message, state: FSMContext):
    await message.answer('Вкажіть перше число:')
    await state.set_state(SumStates.first_number)

@dp.message(SumStates.first_number)
async def cmd_sum_first_num(message: types.Message, state: FSMContext):
    if not message.text.isnumeric():
        await message.answer('Ви ввели некоректне значення! Спробуйте ще раз.')
        return

    await state.update_data(first_number=message.text)
    await message.answer(f'Введіть друге число: ')
    await state.set_state(SumStates.second_number)

@dp.message(SumStates.second_number)
async def cmd_sum_second_num(message: types.Message, state: FSMContext):
    if not message.text.isnumeric():
        await message.answer('Ви ввели некоректне значення! Спробуйте ще раз.')
        return
    first_number = int((await state.get_data())['first_number'])
    second_number = int(message.text)
    await message.answer(f'{first_number} + {second_number} = {first_number + second_number}')
    await state.clear()

# === GENERAL COMMANDS ===
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer('/help – отримати довідку за командами')

@dp.message(Command('roll'))
async def cmd_roll(message: types.Message, command: CommandObject):
    if command.args is not None:
        args = command.args.split()
        await message.answer(f'Випадкове число від 1 до {args[0]}: {random.randint(1, int(args[0]))}')
    else:
        await message.answer(f'Випадкове число від 1 до 100: {random.randint(1, 100)}')

    # await message.reply(text='Help command')


@dp.message()
async def message(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())