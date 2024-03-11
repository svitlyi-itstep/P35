def sum(a, b):
    print(f'{a} + {b} = {a + b}')

def dif(a, b):
    print(f'{a} - {b} = {a - b}')

def mult(a, b):
    return a * b


def tmax(a, b, c, d):
    return max(a, b, c, d)

horizontal = False
symbol = '&'
if horizontal:
    print(symbol * 30)
else:
    print((symbol+'\n') * 30)

# sum(2, 2)
# sum(8, 34)
#
# # a, b = [int(num) for num in input('a, b: ').split()]
#
# # АБО
#
# a = int(input('Введіть перше число:'))
# b = int(input('Введіть друге число:'))
#
# sum(a, b)
# print(mult(a, b))
