import math
X = float(input("Введите объем шара (в кубических единицах): "))
radius = ((3 * X) / (4 * math.pi)) ** (1/3)
print("Радиус шара:", radius)
