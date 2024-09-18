import math
z = float(input("Введите значение z: "))
y = float(input("Введите значение y: "))
cos_diff = math.cos(z) - math.cos(y)
sin_term = (1 + 2 * math.sin(y)) ** (-1/2)
poly_term = 1 + z / 2 + (z ** 3) / 3 + (z ** 4) / 4
w = cos_diff * sin_term * poly_term
print("Значение функции w:", w)