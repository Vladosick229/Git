import math

def trapezoid_area(a, b, c, d):
    # Вычисление полупериметра
    p = (a + b + c + d) / 2
    
    # Вычисление площади по формуле Герона
    area = math.sqrt((p - a) * (p - b) * (p - c) * (p - d))
    return area

# Ввод значений сторон трапеции
a = float(input("Введите длину основания a: "))
b = float(input("Введите длину основания b: "))
c = float(input("Введите длину боковой стороны c: "))
d = float(input("Введите длину боковой стороны d: "))

# Вычисление и вывод площади трапеции
area = trapezoid_area(a, b, c, d)
print(f"Площадь трапеции: {area}")