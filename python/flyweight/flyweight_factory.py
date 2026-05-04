from typing import Dict

from Patterns.python.flyweight.flyweight import Flyweight

class FlyweightFactory():
    """
        Фабрика Легковесов создает объекты-Легковесы и управляет ими. Она 
        обеспечивает правильное разделение легковесов. Когда клиент запрашивает 
        легковес, фабрика либо возвращает существующий экземпляр, либо создает
        новый, если он ещё не существует.
    """
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        """
            Возвращает хеш строки Легковеса для данного состояния
        """
        return "_".join(sorted(state))
    
    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        """
            Возвращает существующий Легковес с заданным состоянием или создает новый
        """

        key = self.get_key(state=shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("Flyweight: Reusing existing flyweight.")

        return self._flyweights[key]
    
    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweight:")
        print("\n".join(map(str, self._flyweights.keys())), end="")