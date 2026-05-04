from Patterns.python.practice.factory_method.creator import Creator
from Patterns.python.practice.factory_method.concrete_creators import ConcreteCreator1, ConcreteCreator2


def client_initialization(creator: Creator) -> None:
    print(f"Конкретный Создатель не известен, но код работает \n"
          "и способен вызвать метод конкретного продукта: \n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print(f"Вызов клиента для создания Продукта 1 \n")
    client_initialization(creator=ConcreteCreator1())

    print("\n")

    print("Вызов клиента для создания Продукта 2 \n")
    client_initialization(creator=ConcreteCreator2())
    print("\n")