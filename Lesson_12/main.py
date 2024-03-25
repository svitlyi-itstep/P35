import random
import time


def factorial(num):
    if num <= 0:
        return 1
    else:
        return num * factorial(num)

def bubble_sort(list):
    is_changed = True
    while is_changed:
        is_changed = False
        for i in range(len(list) - 1):
            if list[i] > list[i +1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                is_changed = True

def quick_sort(list):
    if len(list) < 1:
        return list
    pivot = list[0]
    g_list = []
    l_list = []
    e_list = [pivot]
    for item in list[1:]:
        if item > pivot:
            g_list.append(item)
        elif item < pivot:
            l_list.append(item)
        else:
            e_list.append(item)
    return quick_sort(l_list) + e_list + quick_sort(g_list)

random_list = [random.randint(-99, 99) for _ in range(10000)]
start = time.time()
print(random_list)
bubble_sort(random_list)
print( random_list)
end = time.time()
print(f'time= {round(end - start, 2)}s')
random_list = [random.randint(-99, 99) for _ in range(10000)]
start = time.time()
sorted_list = quick_sort(random_list)
print(sorted_list)
end = time.time()
print(f'time= {round(end - start, 2)}s')
