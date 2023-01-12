"""
Создать мета-класс для паттерна Синглтон.
"""


class Singleton(type):
    """
    Класс Singleton
    """
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyNumber(metaclass=Singleton):
    """
    Класс MyNumber
    """

    def __init__(self, number):
        self.number = number

    def plug_1(self):
        """заглушка"""

    def plug_2(self):
        """заглушка"""


class MyString(metaclass=Singleton):
    """
    Класс MyString
    """

    def __init__(self, m_string):
        self.m_string = m_string + ', World!'

    def plug_1(self):
        """заглушка"""

    def plug_2(self):
        """заглушка"""


num_1 = MyNumber(1)
print(f'num_1 = {num_1.number}')

num_2 = MyNumber(10)
print(f'num_2 = {num_2.number}')

str_1 = MyString('Hello')
print(f'str_1 = {str_1.m_string}')

str_2 = MyString(', World!')
print(f'str_2 = {str_2.m_string}\n')

print(f'num_1 is num_2 — {num_1 is num_2}')
print(f'srt_1 is str_2 — {str_1 is str_2}')
print(f'num_1 is str_2 — {num_1 is str_1}')
print(f'num_2 is str_2 — {num_2 is str_2}')
