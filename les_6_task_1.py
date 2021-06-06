"""
Lesson 2 task 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


import sys


def memory(*args):
    size = 0
    for arg in args:
        size += sys.getsizeof(arg)
        print("Адрес переменной", id(arg))
        if hasattr(arg, '__iter__'):
            if hasattr(arg, 'items'):
                for key, value in x.items():
                    size += memory(key)
                    size += memory(value)
            elif not isinstance(arg, str):
                for item in arg:
                    size += memory(item)
    return size


num = int(input("Введите натуральное число: "))
d_num = num
r_num = 0
while True:
    r_num += d_num % 10
    d_num //= 10
    if d_num > 0:
        r_num *= 10
    else:
        break

print("Решение с помощью чисел")
print("Размер переменной", memory(num), "байт")
print("Размер переменной", memory(r_num), "байт")
print(f"Общий размер переменных {memory(num, r_num)}")
print(r_num)
num_list = list(str(num))

print("Решение с помощью списка")
print("Размер переменной", memory(num_list), "байт")

for i in range(len(num_list)//2):
    num_list[i], num_list[-(i+1)] = num_list[-(i+1)], num_list[i]

print(num_list)
# Тут мне было интересно посмотреть как меняются ссылки на ячейки в массиве
print("Размер переменной", memory(num_list), "байт")
print("Размер переменной", memory(i), "байт")
print(f"Общий размер переменных {memory(i, num_list)}")

print("Решение с помощью строки")
num_str = str(num)
print("Размер переменной", memory(num_str), "байт")
num_str = num_str[::-1]
print(num_str)
print("Размер переменной", memory(num_str), "байт")
print(f"Общий размер переменных {memory(num_str) * 2}")
