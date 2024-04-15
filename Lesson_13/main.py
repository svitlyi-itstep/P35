import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
import random
from aiogram import F

from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from states import SumStates, ButtonStates

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7026397921:AAFpAYDlvhpYlcpBSxOVst4oDv1AueMU7Q4")
dp = Dispatcher()

# === BUTTONS ===
# -- INLINE BUTTONS --

def get_buttons_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='Button 1', callback_data='button_1'),
                types.InlineKeyboardButton(text='Button 2', callback_data='button_2'))
    builder.row(types.InlineKeyboardButton(text='Google', url='https://www.google.com/'))
    return builder
@dp.message(Command("inline_buttons"))
async def cmd_inline_buttons(message: types.Message, state: FSMContext):
    await message.answer('Оберіть дію', reply_markup=get_buttons_keyboard().as_markup())

@dp.callback_query(F.data == 'button_1')
async def button_1_callback(callback: types.CallbackQuery):
    # await callback.message.answer('Ви натиснули кнопку Button 1')
    await callback.message.edit_text('Ви натиснули кнопку Button 1',
                                     reply_markup=get_buttons_keyboard().as_markup())
    # await callback.answer(text='Ви натиснули кнопку Button 1', show_alert=True)
    await callback.answer()

@dp.callback_query(F.data == 'button_2')
async def button_2_callback(callback: types.CallbackQuery):
    # callback.message.text - текст повідомлення
    await callback.message.edit_text('Ви натиснули кнопку Button 2',
                                     reply_markup=get_buttons_keyboard().as_markup())
    await callback.answer()
    await callback.message.delete()


# -- COMMON BUTTONS --
@dp.message(Command("buttons"))
async def cmd_buttons(message: types.Message, state: FSMContext):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text='Button 1'), types.KeyboardButton(text='Button 2'))
    builder.row(types.KeyboardButton(text='Button 3'))

    # keyboard = types.ReplyKeyboardMarkup(
    #     keyboard=[
    #         [types.KeyboardButton(text='Button 1'), types.KeyboardButton(text='Button 2')],
    #         [types.KeyboardButton(text='Button 3')]
    #     ],
    #     resize_keyboard=True
    # )
    await message.answer('Кнопки додано нижче', reply_markup=builder.as_markup(resize_keyboard=True))
    await state.set_state(ButtonStates.choose_button)

@dp.message(ButtonStates.choose_button)
async def onclick_button(message: types.Message, state: FSMContext):
    if message.text.startswith('Button'):
        await message.answer(f'Ви натиснули на кнопку {message.text}',
                             reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
    else:
        await message.answer('Натисніть на кнопку!')

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


# @dp.message()
# async def message(message: types.Message):
#     await message.answer(message.text)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())