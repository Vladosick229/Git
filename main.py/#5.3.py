def time_from_minutes(n):
    # Количество минут в сутках
    minutes_in_day = 24 * 60
    
    # Приведение n к диапазону от 0 до minutes_in_day - 1
    n = n % minutes_in_day
    
    # Вычисление часов и минут
    hours = n // 60
    minutes = n % 60
    
    return hours, minutes

# Ввод количества минут с начала суток
n = int(input("Введите количество минут с начала суток: "))

# Вычисление и вывод времени
hours, minutes = time_from_minutes(n)
print(f"Часы: {hours}, Минуты: {minutes}")