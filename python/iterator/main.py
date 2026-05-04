from Patterns.python.iterator.collection import WordCollections


"""
    Для создания Итератора есть 2 абстрактных класса из встроенного 
    модуля collections - Iterable и Iterator. Необходимо реализовать метод __iter__() в
    итерируемом объекте (списке), а метод __next__() в итераторе.
"""


if __name__ == "__main__":
    # Клиентский код может знать или не знать о Конкретном Итераторе или классах
    # Коллекций, в зависимости от уровня косвенности, который необходим
    # сохранить в программе
    collection = WordCollections()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")