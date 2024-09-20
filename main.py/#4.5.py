import math

def g(z):
    return math.sin(z)

def calculate_h(x, y, z):
    try:
        numerator = x**(y+1) + math.exp(y-1)
        denominator = 1 + abs(y - x)
        term1 = numerator / denominator
        
        abs_diff = abs(y - x)
        term2 = g(z) * ((1 + abs_diff) + (abs_diff**2 / 2) + (abs_diff**3 / 3))
        
        h = term1 - term2
        return h
    except ValueError as e:
        return str(e)

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите значение z: "))

result = calculate_h(x, y, z)
print(f"Значение h: {result}")