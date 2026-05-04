from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass


    def some_operation(self) -> str:
        product = self.factory_method()

        result = f'Creator: код создателя только что работал с {product.operation()}'

        return result