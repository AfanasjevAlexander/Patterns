"""
    Наивный одиночка. 
    Небезопасен в многопоточной среде, т.к. несколько потоков могут одновременно вызвать метод получения Одиночки
    и создать сразу несколько экземпляров объекта.
"""

from typing import Any


class SignletonMeta(type):
    """
    В Python класс Одиночка можно реализовать по-разному. Возможные способы 
    включают себя базовый класс, декоратор, метакласс. 
    Метакласс лучше всего подходит для этой цели.
    """

    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        """
        Данная реализация не учитывает возможное изменение передаваемых аргументов в '__init__'
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Singleton(metaclass=SignletonMeta):
    def some_business_logic(self):
        """
        Любой одиночка должен содержать некоторую бизнес-логику,
        которая может быть выполнена на его экземпляре
        """

if __name__ == "__main__":
    # Клиентский код
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances")