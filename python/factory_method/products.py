from abc import ABC, abstractmethod


class Product(ABC):
    """
        Интерфейс Продукта определяет операции, которые должны выполнять все конкретные продукты
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Конкретные Продукты предоставлют различные реалиции интерфейса Продукта
"""
class ConcreteProduct1(Product):

    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"
    

class ConcreteProduct2(Product):

    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"