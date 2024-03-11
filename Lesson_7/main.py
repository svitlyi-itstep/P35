# while True:
#
#     print('--Menu--')
#     print('1) Action 1')
#     print('2) Action 2')
#     print('3) Action 3')
#     print('0) Exit')
#
#     number = int(input('Оберіть дію:'))
#     if number == 0:
#         break
#     elif number == 1:
#         print('Action 1')
#     elif number == 2:
#         print('Action 2')
#     elif number == 3:
#         print('Action 3')
#     else:
#         print('Введено невірне число!')
#
#
# a = 1
# b = 7
#
# for i in range(a, b + 1):
#     print(i, end='\t')

# /////////////////////////////////////////////

import random
import time

start = time.time()
secret = random.randint(1, 500)

input('Вгадайте число:')
print(f'Загадане число: {secret}')

end = time.time()

print(f'Витрачено {round(end - start, 2)} секунд.')
