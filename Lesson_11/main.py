import tools


# numbers = input_list('Введіть список чисел (через пробіл): ')
numbers = tools.input_list(random=True)
sortByGrowth = tools.input_yes_no('Ви хочете відформатувати список за зростанням? (т/н):')

print(f'Список до сортування: {numbers}')
tools.bubble_sort(numbers, sortByGrowth)
print(f'Список після сортування: {numbers}')

while True:
    print('Do something....')
    if not tools.input_yes_no('Повторити ще раз? (т/н):'):
        break
