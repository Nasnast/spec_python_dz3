# Задача 2. Поиск наибольшего числа в списке
# Напишите программу, которая принимает список чисел через строку и
# возвращает наибольшее число в этом списке.


numbers = [int(a) for a in input("Введите числа через пробел: ").split()]

max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(max_num)
