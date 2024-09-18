import math
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
numerator = (8 + abs(x - y) ** 2) ** (1/3) + 1
denominator = x ** 2 + y ** 2 + 2
exponential = math.exp(x - y)
u = numerator / denominator - exponential
print("Значение функции u:", u)