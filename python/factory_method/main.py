from Patterns.python.factory_method.creator import Creator
from Patterns.python.factory_method.concrete_creators import ConcreteCreator1, ConcreteCreator2


def initialize(creator: Creator) -> None:
    """
        Клиентский код работает с экземпляром конкретного Создателя, хотя и через его базовый интерфейс.
        Пока клиент продолжает работать с создателем через базовый интерфейс, можно передать ему любой подкласс Создателя
    """
    print(f"Client: конкретный класс Creator не известен, но приложение работает\n"
          f"{creator.some_operations()}", end="")



if __name__ == '__main__':
    print("Приложение запущено для ConcreteCreator1.")
    initialize(ConcreteCreator1())
    print("\n")

    print("Приложение запущено для ConcreteCreator2.")
    initialize(ConcreteCreator2())
    print("\n")