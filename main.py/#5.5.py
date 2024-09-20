# Ввод числа
number = input("Введите число из 8 разрядов: ")

# Проверка, что введенное число состоит из 8 цифр
if len(number) != 8 or not number.isdigit():
    print("Пожалуйста, введите корректное число из 8 цифр.")
else:
    # Вычисление суммы цифр числа
    digit_sum = sum(int(digit) for digit in number)
    
    # Вывод результата
    print("Сумма всех цифр числа:", digit_sum)