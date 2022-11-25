"""
Базовое задание:
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в
числе. Для решения используйте цикл while и арифметические операции.
"""

input_num = int(input('Введите целое положительное число: '))
num = input_num
max_num = 0

while num > 0:
    number = num % 10
    num //= 10
    if number > max_num:
        max_num = number

print(f'В числе {input_num} наибольшая цифра: {max_num}')
