from __future__ import annotations
from collections.abc import Iterator
from typing import Any

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Patterns.python.iterator.collection import WordCollections


class AlphabeticalOrderIterator(Iterator):
    """
        Конкретные Итераторы реализуют различные алгоритмы обхода. Эти классы
        постоянно хранят текущее положение обхода
    """

    """
        Атрибут _position хранит текущее положение обхода. У итератора может быть 
        множество других полей для хранения состояния итерации, особенно когда он 
        должен работать с определенным типом коллекции.
    """
    _position: int = None

    """
        Этот атрибут указывает направление обхода
    """
    _reverse: bool = False

    def __init__(self, collection: WordCollections, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        """
            Метод __next__() должен вернуть следующий элемент в последовательности.
            При достижении конца коллекции и в последующих вызовах должно вызываться 
            исключение StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except:
            raise StopIteration()
        
        return value