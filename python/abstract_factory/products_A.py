from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    """
        Каждый отдельный продукт семейства продуктов должен иметь базовый интерфейс
        Все вариации продукта должны реализовывать этот интерфейс
    """


    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
    Конкретные продукты создаются соответствующими Конкретными Фабриками
"""
class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1"
    

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2"