from __future__ import annotations
from Patterns.python.practice.factory_method.creator import Creator
from Patterns.python.practice.factory_method.products import Product, ConcreteProduct1, ConcreteProduct2


class ConcreteCreator1(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct1()
    

class ConcreteCreator2(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct2()