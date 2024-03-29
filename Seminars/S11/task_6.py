"""
---
Базовое задание:
Задание 6.

Создать НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у (ЛЮБОГО!!!) человека при запуске вашего скрипта.

При сдаче задания в папке должен лежать текстовый файл!

Это значит вы должны предусмотреть случай, что вы по дефолту записали файл в cp1251,
а прочитать пытаетесь в utf-8.

Преподаватель будет запускать ваш скрипт и ошибок НЕ ДОЛЖНО появиться!

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке,
но открыть нужно ИМЕННО!!! в формате Unicode (utf-8)
--- обратите внимание на чтение файла в режиме rb
для последующей конвертации в нужную кодировку
"""
from chardet import detect


def my_func():
    """
    Определение кодировки файла test_file.txt, конвертация в UTF-8 и
    вывод содержимого файла в терминал.
    """
    with open('test_file.txt', 'rb') as f_obj:
        content_bytes = f_obj.read()
    encoding = detect(content_bytes)['encoding']
    print(f'Кодировка файла {f_obj.name}: {encoding}')
    if encoding != 'utf-8':
        print(f'Конвертация кодировки {encoding} в utf-8.')
        content_text = content_bytes.decode(encoding)
        with open('test_file.txt', 'w', encoding='utf-8', newline='') as f_obj:
            f_obj.write(content_text)
    print(f'\nСодержимое файла {f_obj.name}:')
    with open('test_file.txt', encoding='utf-8') as f_obj:
        print(f'{f_obj.read()}')


my_func()
