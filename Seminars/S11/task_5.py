"""
---
Базовое задание:
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet.
"""
import subprocess as sp
import chardet

args_1 = ['ping', 'yandex.ru']
with sp.Popen(args_1, stdout=sp.PIPE) as ya_ping:
    for line in ya_ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding'])
        print(line)

args_2 = ['ping', 'youtube.com']
with sp.Popen(args_2, stdout=sp.PIPE) as yt_ping:
    for line in yt_ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding'])
        print(line)
