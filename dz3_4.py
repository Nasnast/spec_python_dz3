# Задача 4. Генерация паролей
# Напишите программу, которая генерирует случайный пароль заданной длины,
# состоящий из букв, цифр и специальных символов.

import random
import string


lenght = int(input("введите длину пароля: "))

password = []
chars = string.ascii_letters + string.digits + string.punctuation
# 1
for _ in range(lenght):
    password.append(random.choice(chars))
print("".join(password))

# 2
password2 = [random.choice(chars) for _ in range(lenght)]
print("".join(password2))
