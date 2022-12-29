"""
---
Базовое задание:
4. Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в
базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    """
    Базовый класс Car.
    """

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def start(self):
        """
        Метод вывода сообщения о начале движения.
        """
        print(f'{self.name} начал движение.')

    def stop(self):
        """
        Метод вывода сообщения об остановке.
        """
        print(f'{self.name} остановился.')

    def turn(self, direction):
        """
        Метод вывода сообщения об изменении направления движения.
        """
        print(f'{self.name} повернул на{direction}.')

    def show_speed(self):
        """
        Метод вывода скорости
        """
        print(f'Скорость {self.name}: {self.speed} км/ч.')


class TownCar(Car):
    """
    Дочерний класс TownCar.
    """
    speed_limit = 60

    def show_speed(self):
        if self.speed >= self.speed_limit:
            print(f'Скорость {self.name}: {self.speed} км/ч.    <<< '
                  f'превышено допустимое значение скорости {self.speed_limit} км/ч.')
        else:
            print(f'Скорость {self.speed} км/ч.')


class SportCar(Car):
    """
    Дочерний класс SportCar.
    """
    speed_limit = 120

    def show_speed(self):
        if self.speed >= self.speed_limit:
            print(f'Скорость {self.name}: {self.speed} км/ч.    <<< '
                  f'превышено допустимое значение скорости {self.speed_limit} км/ч.')
        else:
            print(f'Скорость {self.speed} км/ч.')


class WorkCar(Car):
    """
    Дочерний класс WorkCar.
    """
    speed_limit = 40

    def show_speed(self):
        if self.speed >= self.speed_limit:
            print(f'Скорость {self.name}: {self.speed} км/ч.    <<< '
                  f'превышено допустимое значение скорости {self.speed_limit} км/ч.')
        else:
            print(f'Скорость {self.speed} км/ч.')


class PoliceCar(Car):
    """
    Дочерний класс PoliceCar.
    """
    is_police = True

    def stop(self):
        if self.speed >= 1236:
            print(f'{self.name} преодолел звуковой барьер и покинул страну.')
        else:
            print(f'{self.name} остановился.')


town_car = TownCar('Ford', 'Чёрный', 40, False)
town_car.start()
town_car.show_speed()
town_car.turn('право')
town_car.turn('лево')
town_car.speed *= 2
town_car.show_speed()
town_car.stop()

print()

sport_car = SportCar('Maserati', 'Красный', 80, False)
sport_car.start()
sport_car.show_speed()
sport_car.turn('лево')
sport_car.speed *= 2
sport_car.show_speed()
sport_car.turn('право')
sport_car.stop()

print()

work_car = WorkCar('LADA', 'Белый', 30, False)
work_car.start()
work_car.show_speed()
work_car.turn('право')
work_car.turn('лево')
work_car.stop()

print()

police_car = PoliceCar('UAZ', 'Серый', 206, True)
police_car.start()
police_car.show_speed()
police_car.turn('лево')
police_car.turn('право')
police_car.turn('лево')
police_car.turn('право')
police_car.speed *= 2
police_car.show_speed()
police_car.turn('лево')
police_car.turn('право')
police_car.turn('лево')
police_car.speed *= 3
police_car.show_speed()
police_car.turn('право')
police_car.turn('лево')
police_car.turn('право')
police_car.stop()
