from abc import ABC, abstractmethod

from Patterns.python.abstract_factory.products_A import AbstractProductA


class AbstractProductB(ABC):
    """
        Базовый интерфейс другого продукта. Все продукты могут взаимодействовать друг с другом,
        но правильное взаимодействие возможно только между продуктами одной и той же конкретной вариации
    """

    @abstractmethod
    def useful_function_b(self) -> None:
        """
            Продукт В способен работать самостоятельно ...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
            ... а также взаимодейстовать с продуктами А той же вариации.

            Абстрактная Фабрика гарантирует, что все продукты, которые она создает,
            имеют одинаковую вариацию и, следовательно, совместимы
        """
        pass

"""
    Конкретные Продукты создаются соответствующими Конкретными Фабриками
"""
class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1"
    
    """
        Продукт В1 может корректно работать только с Продуктом А1. Тем не менее, 
        он принимает любой экземпляр Абстрактного Продукта А в качестве аргумента
    """
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the {result}"
    
class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2"
    
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        """
            Продукт В2 может корретно работать только с продуктом А2. Тем не менее,
            он принимает любой экземпляр Абстрактного Продукта А в качестве аргумента
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the {result}"