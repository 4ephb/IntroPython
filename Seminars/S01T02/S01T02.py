"""
Семинар 01
---
Базовое задание:
2. Пользователь вводит время в секундах. Программа переводит время в часы,
минуты и секунды и выводит в формате чч:мм:сс
"""

input_sec = int(input('Введите время в секундах: '))

hours = input_sec // 3600
minutes = int((input_sec % 3600) / 60)
seconds = int((input_sec % 3600) % 60)

if hours < 10:
    hours = str(f'0{hours}')
if minutes < 10:
    minutes = str(f'0{minutes}')
if seconds < 10:
    seconds = str(f'0{seconds}')

print(f"{hours}:{minutes}:{seconds}")
