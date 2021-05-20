"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


def sum_c(count):
    n = 1
    sum_n = 0
    dif = -0.5
    while True:
        if count > 0:
            sum_n += n
            n *= dif
            count -= 1
        else:
            return sum_n


a = int(input("Введете натуральное число"))
print(sum_c(a))
