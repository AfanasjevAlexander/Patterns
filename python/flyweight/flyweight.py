import json

class Flyweight():
    """
        Легковес хранит общую часть состояния (также называемую внутренним 
        состоянием), которая пренадлежит нескольким реальным бизнес-объектам.
        Легковес принимает оставшуюся часть состояния (внешнее состояние,
        уникальное для каждого объекта) через его параметры метода
    """

    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        dump_state = json.dumps(self._shared_state)
        dump_unique_state = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({dump_state}) and unique ({dump_unique_state}) state.", end="")