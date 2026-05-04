from Patterns.python.bridge.implementations import Implementation

class Abstraction:
    """
        Абстракция устанавливает интерфейс для "управляющей" части двух иерархий классов. 
        Она содержит ссылку на объект из иерархии Реализации и делегирует ему всю настоящую работу
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implenetation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with: \n"
                f"{self.implenetation.operation_implementation()}")
    

class ExtendedAbstraction(Abstraction):
    """
        Можно расширить Абстракцию без изменения классов Реализации
    """

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with: \n"
                f"{self.implenetation.operation_implementation()}")