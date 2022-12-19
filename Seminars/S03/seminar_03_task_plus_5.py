"""
---
Дополнительное задание:
5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
[Негафибоначчи] https://vk.cc/cjn95T
"""


def fibonacci(num):
    """
    Функция составляет список чисел Фибоначчи, в том числе для отрицательных индексов.
    num - входящее значение. int()
    result - итоговый список чисел Фибоначчи. list()
    """
    result = [-1, 1, 0, 1, 1]  # Значения для k = -2, -1, 0, 1, 2
    for i in range(len(result) + 1, num + 4):
        result.insert(-i, result[-i + 2] - result[-i + 1])
    for i in range(len(result), num + len(result) - 2):
        result.append(result[i - 1] + result[i - 2])
    return result


k_num = int(input('Введите число: '))
print(f'{k_num} -> {fibonacci(k_num)}')
