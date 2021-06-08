"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random


def sort_bubble(data):
    check = True
    for i in range(len(data)):
        if check:
            check = False
            for j in range(len(data) - i - 1):
                if data[j] < data[j + 1]:
                    check = True
                    data[j], data[j + 1] = data[j + 1], data[j]


MIN = -100
MAX = 100
LENGTH = 10
array = [random.randint(MIN, MAX-1) for _ in range(LENGTH)]

print(array)
sort_bubble(array)
print(array)
