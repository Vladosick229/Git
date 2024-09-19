import math

def calculate_beta(x, y, z):
    try:
        if z < -1 or z > 1:
            raise ValueError("Значение z должно быть в диапазоне от -1 до 1 для функции arcsin.")
        
        beta = math.sqrt(10 * (3 * math.sqrt(x) + x**(2/5)) * (math.asin(z) - abs(x - y))**2)
        return beta
    except ValueError as e:
        return str(e)

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите значение z: "))

result = calculate_beta(x, y, z)
print(f"Значение β: {result}")