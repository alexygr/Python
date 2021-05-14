"""
По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков.
Если такой треугольник существует, то определить,
является ли он разносторонним, равнобедренным или равносторонним.
"""

print("Введите длину трёх отрезков треугольник")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a + b) > c and (a + c) > b and (c + b) > a:
    if a == b == c:
        print("Это равносторонний треугольник")
    elif a == c or a == b or c == b:
        print("Это равнобедренной треугольник")
    else:
        print("Это разносторонний треугольник")
else:
    print("Треугольник не может быть составлен")
