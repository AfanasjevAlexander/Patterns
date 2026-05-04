from __future__ import annotations
from collections.abc import Iterable
from typing import Any

from Patterns.python.iterator.iterator import AlphabeticalOrderIterator



class WordCollections(Iterable):
    """
        Конкретные Коллекции предоставляют один или несколько методов для получения
        новых экземпляров итератора, совместимых с классом коллекции
    """

    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []
        
    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
            Метод __iter__() возвращает объект итератора, по умолчанию возвращаем
            итератор с сортировкой по возрастанию
        """
        return AlphabeticalOrderIterator(self)
    
    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, True)
    
    def add_item(self, item: Any) -> None:
        self._collection.append(item)