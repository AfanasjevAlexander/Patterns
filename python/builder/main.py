from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
        Интерфейс строителя объявляет создающие методы для различных частей объектов Продукты
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """
        Классы Конкретного строителя следует интерфейсу Строителя и предоставляет конкретные реализации шагов построения.
        Можно создавать много Конкретных Строителей, реализованных по-разному
    """

    def __init__(self) -> None:
        """
            Новый экземпляр Строителя должен содержать пустой объект Продукта,
            который будет использоваться в дальнейшей сборке
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    
    @property
    def product(self) -> Product1:
        """
            Конкретные Строители должны предоставить свои собственные методы получения результатов. 
            Это связано с тем, что различные типы строителей могут создавать совершенно разные продукты с разными интерфейсами.
            Поэтому такие методы не могут быть объявлены в базовом интерфейсе Строителя
            (по крайне мере, в статически типизированных языках программирования)  

            Как правило, после возвращения конечного результата Клиенту, экземпляр Строителя
            должен быть готов к началу производства следующего Продукта. 
            Поэтому обычной практикой является вызов метода сброса в конце тела метода getProduct.
            Однако такое поведение не является обязательным, можно заставить ожидать Строителей 
            явного запроса на сброс из кода клиента, прежде чем избавиться от предыдущего результата.
        """
        product = self._product
        self.reset()
        return product
    
    def produce_part_a(self) -> None:
        return self._product.add("PartA1")
    
    def produce_part_b(self) -> None:
        return self._product.add("PartB1")
    
    def produce_part_c(self) -> None:
        return self._product.add("PartC1")
    

class Product1():
    """
        Паттерн Строитель имеет смысл только тогда, когда Продукты достаточно сложны и 
        требуют обширной конфигурации.

        В отличии от других Пораждающих Паттернов, различные Конкретные Строители могут производить несвязанные Продукты.
        Другими словами, результаты различных строителей могут не всегда следовать одному и тому же интерфейсу
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Products parts: {', '.join(self.parts)}", end="")

class Director():
    """
        Директор отвечает только за выполнение шагов построения в определённой последовательности.
        Это полезно при производстве Продуктов в определённом порядке или особой конфигурации. 
        Класс Директор необязателен, т.к. клиент может напрямую управлять Строителями
    """

    def __init__(self) -> None:
        self._builder = None

    @property 
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
            Директор работает с любым элементом строителя, который передаётся ему клиентским кодом. Таким образом,
            клиентский код может изменить конечный тип вновь собираемого продукта
        """
        self._builder = builder

    """
        Директор может строить несколько вариаций продукта, используя одинаковые шаги построения
    """
    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()



if __name__ == "__main__":
    """
        Клиентский код создает объект Строитель, передает его Директору и иницирует процесс построения.
        Конечный результат извлекается из объекта-Строителя.
    """
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standart basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standart full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Строитель можно использовать без класса Директор
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
