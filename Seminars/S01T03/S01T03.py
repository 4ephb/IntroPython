"""
Базовое задание:
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
"""

num = int(input('Введите число: '))
num2 = int(f'{num}{num}')
num3 = int(f'{num}{num}{num}')

print(f'{num} + {num2} + {num3} =', num + num2 + num3)