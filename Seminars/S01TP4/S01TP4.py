"""
Дополнительное задание:
4. Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
"""

qrt_num = int(input("Введите номер четверти: "))

if qrt_num < 1 or qrt_num > 4:
    print("Введите числа от 1 до 4!")
elif qrt_num == 1:
    print("(x > 0; y > 0)")
elif qrt_num == 2:
    print("(x < 0; y > 0)")
elif qrt_num == 3:
    print("(x < 0; y < 0)")
elif qrt_num == 4:
    print("(x > 0; y < 0)")
