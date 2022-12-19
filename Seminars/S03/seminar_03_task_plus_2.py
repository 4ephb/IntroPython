"""
---
Дополнительное задание:
2. Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
"""


def prod_pairs_list(in_list):
    """
    in_list - Входящее значение. list()
    new_len - Длинна нового списка
    new_list - Новый список из произведений пар чисел списка in_list
    """
    new_len = len(in_list) // 2 + 1 if len(in_list) % 2 != 0 else len(in_list) // 2
    new_list = [in_list[i] * in_list[len(in_list) - i - 1] for i in range(new_len)]
    return new_list


input_list = [2, 3, 4, 5, 6]

print(f'{input_list} => {prod_pairs_list(input_list)}')
