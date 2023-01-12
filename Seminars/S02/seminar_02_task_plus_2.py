"""
---
Дополнительное задание:
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""


def get_int(message: str) -> int:
    return int(input(message))


n = get_int('Введите число от 1 до N: ')

res = []
for i in range(1, n + 1):
    if i == 1:
        res.append(i)
    else:
        res.append(i * res[-1])

print(f'Пусть N = {n}, тогда {res}')
