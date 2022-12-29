"""
Семинар 03
---
Дополнительное задание:
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
45 -> 101101
3 -> 11
2 -> 10
"""


def dec_to_bin_1(input_num):
    """
    Первоначальное решение через while.
    """
    bin_num = ""
    while input_num != 0:
        bin_num = str(input_num % 2) + bin_num
        input_num //= 2
    if not bin_num:
        bin_num = "0"
    return bin_num


print(dec_to_bin_1(42))


def dec_to_bin_2(input_num):
    """
    Оптимизированное решение с помощью функции bin.
    """
    return bin(input_num)


print(dec_to_bin_2(42))
