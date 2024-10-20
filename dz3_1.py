# Задание 1. Удаление дубликатов из списка
# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.


elements = [1, 1, 1, 3, 2, 3, 4, 5, 1, 2, 2, 2, 2]
print(f"Исходный список: {elements}")

dublicat = []

for el in elements:
    if elements.count(el) != 1 and el not in dublicat:
        dublicat.append(el)
print(f"Список дублирующих элементов: {dublicat}")
