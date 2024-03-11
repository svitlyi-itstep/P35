import random as rnd


def input_list(message='', random=False):
    if random:
        return [rnd.randint(-50, 50) for _ in range(10)]
    while True:
        numbers = [int(number) for number in input(message).split()]
        if not numbers:
            print('Ви нічого не ввели!')
        else:
            return numbers


def input_yes_no(message):
    while True:
        answer = input(message).lower()
        if answer not in ('т', 'так', 'y', 'yes', '+', 'н', 'ні', 'n', 'no', '-'):
            print('Некоректна відповідь!')
        else:
            return answer in ('т', 'так', 'y', 'yes', '+')


def bubble_sort(list, sortByGrowth):
    is_changed = True
    while is_changed:
        is_changed = False
        for i in range(len(list) - 1):
            if (list[i] > list[i + 1] and sortByGrowth) or \
                    (list[i] < list[i + 1] and not sortByGrowth):
                list[i], list[i + 1] = list[i + 1], list[i]
                is_changed = True
