
a = 6
b = 2

if b == 0:
    print('На нуль ділити не можна!')
if b != 0:
    print(a / b)
'''
2 % 2 = 0
3 % 2 = 1

if a % 2 == 0:

message = input('Введіть повідомлення:')

if not message:
    print('Ви нічого не ввели')
else:
    print('Введене вами повідомлення:', message
'''

print('Дії:')
print('1. Дія 1')
print('2. Дія 2')

choise = int(input('Оберіть дію: '))

if choise == 1:
    print('Дія 1')
elif choise == 2:
    print('Дія 2')
else:
    print('Некоректний вибір')