from Patterns.python.abstract_factory.factories import AbstractFactory, ConcreteFactory1, ConcreteFactory2

def initialize(factory: AbstractFactory) -> None:
    """
        Клиентский код работает с Фабриками и Продуктами только через абстрактные типы: Абстрактная Фабрика и Абстрактный продукт.
        Это позволяет передавать любой подкласс фабрики или продукта клиентскому коду, не нарушая его.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"init_1: {product_b.useful_function_b()}")
    print(f"init_2: {product_b.another_useful_function_b(product_a)}", end="")



if __name__ == "__main__":
    """
        Клиентский код может работать с любым конкретным классом фабрики 
    """
    print("Client: Testing client code with the first factory type:")
    initialize(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    initialize(ConcreteFactory2())