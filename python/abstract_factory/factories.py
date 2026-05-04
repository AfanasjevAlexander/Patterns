from abc import ABC, abstractmethod

from Patterns.python.abstract_factory.products_A import AbstractProductA, ConcreteProductA1, ConcreteProductA2
from Patterns.python.abstract_factory.products_B import AbstractProductB, ConcreteProductB1, ConcreteProductB2


class AbstractFactory(ABC):
    """
        Интерфейс Абстрактной Фабрики объявляет наборы методов, которые возвращают различные абстрактные продукты. 
        Эти продукты называют семейством и связаны темой/концепцией высокого уровня. Продукты одного семейства обычно 
        могут взаимодействовать между собой. 
        Семейство продуктов может иметь несколько вариаций, но продукты одной вариации не совместимы с продуктами другой.
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
        Конкретная фабрика производит семейство продуктов одной вариации, при этом гарантирует совместимость полученных продуктов.
        Сигнатуры методов Конкретной Фабрики возвращают абстрактный продукт, 
        в то время как внутри метода создается экземпляр конкретного продукта 
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()
    

class ConcreteFactory2(AbstractFactory):
    """
        Каждая Конкретная Фабрика имеет соответствующую вариацию продукта
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()