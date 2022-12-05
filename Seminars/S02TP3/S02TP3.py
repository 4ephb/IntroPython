"""
---
Дополнительное задание:
3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
Пример:
Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""


def get_int(message: str) -> int:
    return int(input(message))


n = get_int('Введите число: ')

list_number = []
for i in range(1, n + 1):
    list_number.append(round((1 + 1 / i) ** i, 2))

result = f'Для n = {n}: {{1: {list_number[0]}'
for i in range(1, n):
    result += f', {i + 1}: {list_number[i]:}'
result += '}' + f' сумма чисел последовательности (1+1 n)^n равна {sum(list_number)}'

print(result)
