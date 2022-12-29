"""
---
Базовое задание:
1.  Создать класс TrafficLight (светофор) и определить у него один атрибут
color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный,
желтый, зеленый. Продолжительность первого состояния (красный) составляет
7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше
усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера,
создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его
нарушении выводить соответствующее сообщение и завершать скрипт.
"""

from time import sleep


class TrafficLight:
    """
    Аттрибуты класса
    """
    __color = {'Красный': 7, 'Жёлтый ': 2, 'Зелёный': 1}

    def run(self):
        """
        Метод сменяющий цвет с задержкой (сек).
        """
        for color, sec in self.__color.items():
            print(f'[ {color} ]')
            sleep(sec)

    def plug(self):
        """заглушка"""


TrafficLight().run()
