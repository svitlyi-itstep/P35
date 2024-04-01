from aiogram.fsm.state import StatesGroup, State


class SumStates(StatesGroup):
    first_number = State()
    second_number = State()


'''
    Переробити бота таким чином, щоб при
    введенні команди /calc у користувача
    запитувалися числа і дія, яку треба
    з ними виконати (+, -, *, /).
    
    Введені числа та операцію перевіряти
    на коректність.

'''