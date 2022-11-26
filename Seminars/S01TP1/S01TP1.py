"""
Дополнительное задание:
1. Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
6 -> да
7 -> да
1 -> нет
"""

while True:
    number = input('Введите день недели: ')
    if number.isdigit():
        number = int(number)
        if 1 <= number <= 7:
            break
    print('Введите число от 1 до 7.')

if 1 <= number <= 5:
    print(f'{number} -> нет')
elif 6 <= number <= 7:
    print(f'{number} -> да')