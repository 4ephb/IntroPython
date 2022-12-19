"""
---
Дополнительное задание:
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
45 -> 101101
3 -> 11
2 -> 10
"""


def dec_to_bin(input_num):
    """
    input_num - Входящее значение. int()
    bin_num - бинарное представление числа input_num
    """
    bin_num = ""
    while input_num != 0:
        bin_num = str(input_num % 2) + bin_num
        input_num //= 2
    if not bin_num:
        bin_num = "0"
    return bin_num


num = int(input("Введите число: "))
print(f'{num} -> {dec_to_bin(num)}')
