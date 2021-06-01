"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
(т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import namedtuple

Venture = namedtuple('Venture', 'name, q1, q2, q3, q4, profit, ga')

count = int(input("Введите количество предприятий"))
_sum = 0
v = []
for i in range(count):
    name = input(f"Введите имя {i+1}-го предприятия")
    pr1 = float(input("Введите прибыль за 1-й квартал"))
    pr2 = float(input("Введите прибыль за 2-й квартал"))
    pr3 = float(input("Введите прибыль за 3-й квартал"))
    pr4 = float(input("Введите прибыль за 4-й квартал"))
    pr_sum = pr1 + pr2 + pr3 + pr4
    v.append(Venture(name, pr1, pr2, pr3, pr4, pr1+pr2+pr3+pr4, None))
    _sum += v[-1].profit

evrg = _sum/count
for i in range(count):
    if v[i].profit > evrg:
        v[i] = v[i]._replace(ga=True)
    elif v[i].profit < evrg:
        v[i] = v[i]._replace(ga=False)
print(f"Средняя прибыль за год всех предприятий - {evrg}")
print("Предприятия с прибылью выше среднего")
for item in v:
    if item.ga:
        print(f"{item.name} - {item.profit}")
print("Предприятия с прибылью ниже среднего")
for item in v:
    if not item.ga:
        print(f"{item.name} - {item.profit}")