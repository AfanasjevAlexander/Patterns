from Patterns.python.bridge.abstractions import Abstraction, ExtendedAbstraction
from Patterns.python.bridge.implementations import ConcreteImplementationA, ConcreteImplementationB


def client_code(abstraction: Abstraction):
    """
    За исключением этапа инициализации, когда объект Абстракции связыватся с 
    определенным объектом Реализации, клиентский код должен зависить только от класса Абстракции.
    Таким образом, клиентский код может поддерживать любую комбинацию абстракции и реализации.
    """

    # some code

    print(abstraction.operation(), end="")

    # some code


if __name__ == "__main__":
    """
        Клиентский код должен работать с любым предварительно сконфигурированной 
        комбинацией абстракции и реализации.
    """

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation=implementation)
    client_code(abstraction=abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation=implementation)
    client_code(abstraction)

    print("\n")