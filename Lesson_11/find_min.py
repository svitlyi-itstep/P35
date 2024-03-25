import random


def find_min(numbers):
    minimum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


numbers = [random.randint(-50, 50) for _ in range(10)]

print(numbers)

minimum = find_min(numbers)

print(minimum)