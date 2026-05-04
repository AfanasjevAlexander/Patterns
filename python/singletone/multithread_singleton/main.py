from threading import Lock, Thread
from typing import Any

class SingletonMeta(type):
    """
        Потокобезопасная реализация класса Singleton
    """

    _instances = {}

    """
        Объект-блокировка для синхронизации потоков во время первого доступа к Одиночке
    """
    _lock: Lock = Lock()

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        """
            Данная реализация не учитывает возможное изменение параметров переданных в '__init__'.

            Установление блокировки самым 'быстрым' потоком
        """
        with cls._lock:
            """
                Первый поток достигает этого условия и ставит блокировку, создавая объект-одиночку.
                Следующий поток тоже ставит блокировку, но т.к. инстанс уже создан, то он и возвращается
            """
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwds)
                cls._instances[cls] = instance
        
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    # используем это поле чтобы показать, что Одиночка работает в многопоточном режиме
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self) -> None:
        """
            Любой Одиночка должен содержать бизнес-логику, 
            которая может быть выполнена на его экземпляре
        """

def test_singleton(value: str) -> None:
    singleton = Singleton(value=value)
    print(singleton.value)


if __name__ == "__main__":
    # client code

    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")
    
    thread_1 = Thread(target=test_singleton, args=("FOO",))
    thread_2 = Thread(target=test_singleton, args=("BAR",))

    thread_1.start()
    thread_2.start()