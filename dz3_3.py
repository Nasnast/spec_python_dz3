# Задача 3. Проверка палиндрома
# Напишите программу, которая принимает строку и определяет, является ли она
# палиндромом (читается одинаково с обеих сторон)

text = input("введите текст: ")

new_text = text.lower().replace(" ", "").replace(",", "").replace("-", "")

if new_text == new_text[::-1]:
    print(f"да")
else:
    print(f"нет")
