"""
Lesson 2 task 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


import sys


def memory(x):
    size = sys.getsizeof(x)
    print("Адрес переменной", id(x))
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += memory(key)
                size += memory(value)
        elif not isinstance(x, str):
            for item in x:
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
print(r_num)
num_list = list(str(num))

print("Решение с помощью списка")
print("Размер переменной", memory(num_list), "байт")

for i in range(len(num_list)//2):
    num_list[i], num_list[-(i+1)] = num_list[-(i+1)], num_list[i]

print(num_list)
print("Размер переменной", memory(num_list), "байт")
print("Размер переменной", memory(i), "байт")

print("Решение с помощью строки")
num_str = str(num)
print("Размер переменной", memory(num_str), "байт")
num_str = num_str[::-1]
print(num_str)
print("Размер переменной", memory(num_str), "байт")
