"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import Counter


def hexa_sum(x, y):
    x = x[::-1]
    y = y[::-1]

    if len(x) > len(y):
        y += '0' * (len(x) - len(y))
    else:
        x += '0' * (len(y) - len(x))

    _sum = []
    m = 0
    for i, j in zip(x, y):
        n = m + hexa[i] + hexa[j]
        if n > 15:
            m = n // 16
            n %= 16
        else:
            m = 0
        _sum += str(hexa[n])
    if m > 0:
        _sum += hexa[m]
    return _sum[::-1]


def hexa_mult(x, y):
    x = x[::-1]

    _mult = []
    m = 0
    for i in x:
        n = m + hexa[i] * hexa[y]
        if n > 15:
            m = n // 16
            n %= 16
        else:
            m = 0
        _mult += str(hexa[n])
    if m > 0:
        _mult += hexa[m]
    return _mult[::-1]


hexa = Counter({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
                0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'})


a = list(input("Видите 1-е шестнадцатиричное число: "))
b = list(input("Видите 2-е шестнадцатиричное число: "))

# a + b
print(a, b)

print(f"Сумма чисел {a} и {b} равна {hexa_sum(a, b)}")
answer = ""
# a * b
for item in range(1, len(a)+1):
    answer = hexa_sum(hexa_mult(b, a[-item])+(['0'] * (item-1)), answer)


print(f"Произведение чисел {a} и {b} равна {answer}")