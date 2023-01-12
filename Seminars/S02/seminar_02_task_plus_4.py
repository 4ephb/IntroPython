"""
---
Дополнительное задание:
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле seminar_02_task_plus_4_file.txt в одной строке одно число.
"""

import random

FILE_NAME = 'seminar_02_task_plus_4_file.txt'


def get_int(message: str) -> int:
    while True:
        try:
            message.isdigit()
            return int(input(message))
        except ValueError:
            print("Ошибка ввода! Введите числовое значение.")


n = get_int('Задайте список из N элементов, заполненных числами из промежутка [-N, N].\nВведите значение N: ')
list_n = []
for i in range(0, n):
    list_n.append(random.randint(-n, n))

data = open(FILE_NAME, "r")
data_pos = data.readlines()
result = 1
num_pos = []
num_items = []
err_pos = 0
for el in data_pos:
    try:
        result *= int(list_n[int(el) - 1])
        num_pos.append(el.split('\n')[0])
        num_items.append(list_n[int(el) - 1])
    except ValueError:
        err_pos += 1
data.close()

print(f'Список: {list_n}\n\n'
      f'В {FILE_NAME} обнаружено {len(num_items)} соответствий и {err_pos + 1} ошибок.\n'
      f'Позиции элементов: {num_pos[:len(num_items)]}\n\n'
      f'Итог: {num_items}\nПроизведение итоговых элементов списка: {result}\n')
