from __future__ import annotations
from Patterns.python.factory_method.creator import Creator

from Patterns.python.factory_method.products import Product, ConcreteProduct1, ConcreteProduct2

"""
    Конкретные Создатели переопределяют фабричный метод для того, 
    чтобы изменить тип результирующего продукта
"""


class ConcreteCreator1(Creator):
    """
        Сигнатура метода по-прежнему использует тип абстракного продукта, хотя фактически из метода возвращается конкретный продукт.
        Таким образом Создатель может оставаться независимым от конкретных классов Продуктов
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()
    

class ConcreteCreator2(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct2()