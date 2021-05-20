"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def sum_d(a):
    sum_a = 0
    while a > 0:
        sum_a += a % 10
        a //= 10
    return sum_a


print("Введи количество вводимых чисел")
max_s = 0
max_n = 0
quantity = int(input(": "))

while quantity > 0:
    number = int(input("Введи натуральное число: "))
    m = sum_d(number)
    if m > max_s:
        max_s = m
        max_n = number
    quantity -= 1
print(f"{max_n} - {max_s }")
