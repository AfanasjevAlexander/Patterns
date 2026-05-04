from abc import ABC, abstractmethod


class Implementation(ABC):
    """
        Реализация устанавливает интерфейс для всех классов реализации. Он не должен 
        соответствовать интерфейсу абстракций. На практике оба интерфейса могут быть совершенно разными.
        Как правило, интерфейс Реализации предоставляет только примитивные операции, в то время как Абстракция
        определяет операции более высокого уровня, основанные на этих примитивах.  
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


"""
Каждая Конкретная Реализация соответствует определенной платформе и реализует 
интерфейс Реализации с использованием API этой платформы. 
"""

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return f"ConcreteImplementationA: Here's the result on the platform A."
    
class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return f"ConcreteImplementationB: Here's the result on the platform B."