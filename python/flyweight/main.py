from Patterns.python.flyweight.flyweight_factory import FlyweightFactory

def add_car_to_police_database(factory: FlyweightFactory, 
                               plates: str,
                               owner: str,
                               brand: str,
                               model: str,
                               color: str) -> None:
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    # Клиентский код либо сохраняет, либо вычисляет внешнее состояние и передает 
    # его методам легковеса.
    flyweight.operation([plates, owner])

    
if __name__ == "__main__":
    """
        Клиентский код обычно создает кучу предварительно заполненых легковесов на этапе инициализации приложения
    """
    factory = FlyweightFactory([["Chevrolet", "Camaro2018", "pink"],
                                ["Mercedes Benz", "C300", "black"],
                                ["Mercedes Benz", "C500", "red"],
                                ["BMW", "M5", "red"],
                                ["BMW", "X6", "white"],
                               ])
    factory.list_flyweights()

    add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "X1", "red")  

    print("\n")
    factory.list_flyweights()  