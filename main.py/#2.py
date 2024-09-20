n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))
apples_per_student = k // n
apples_left_in_basket = k % n
print("Каждому школьнику достанется:", apples_per_student)
print("Яблок останется в корзинке:", apples_left_in_basket)