from abc import ABC, abstractmethod


"""
Паттерн Абстрактная Фабрика предоставляет интерфейс создания
семейств взаимосвязанных или взаимозависимых объектов без указания их конкретных классов.
"""


class Cafe(ABC):
    @abstractmethod
    def create_pizza(self) -> "AbstractPizza":
        pass

    @abstractmethod
    def create_coffee(self) -> "AbstractCoffee":
        pass


"""
Задача конкретных фабрик — создавать ингредиенты для пиццы.
Каждая фабрика умеет создавать пра- вильные объекты для своего региона.
"""


class MinskCafe(Cafe):
    def create_pizza(self) -> "AbstractPizza":
        return MinskPizza()

    def create_coffee(self) -> "AbstractCoffee":
        return MinskCoffee()


class GomelCafe(Cafe):
    def create_pizza(self) -> "AbstractPizza":
        return GomelPizza()

    def create_coffee(self) -> "AbstractCoffee":
        return GomelCoffee()


class AbstractPizza(ABC):
    """
    Каждый отдельный продукт семейства продуктов должен иметь базовый интерфейс.
    Все вариации продукта должны реализовывать этот интерфейс.
    """

    @abstractmethod
    def logotype(self) -> str:
        pass


"""
Конкретные продукты создаются соответствующими Конкретными Фабриками.
"""


class MinskPizza(AbstractPizza):
    def logotype(self) -> str:
        return f"MinskPizza logotype is signed"


class GomelPizza(AbstractPizza):
    def logotype(self) -> str:
        return f"GomelPizza logotype is signed"


class AbstractCoffee(ABC):
    @abstractmethod
    def logotype(self):
        pass

    @abstractmethod
    def barista_picture(self):
        pass


class MinskCoffee(AbstractCoffee):
    def logotype(self) -> str:
        return f"MinskCoffee logotype is signed"

    def barista_picture(self):
        return f"MinskCoffee barista was draw"


class GomelCoffee(AbstractCoffee):
    def logotype(self) -> str:
        return f"GomelCoffee logotype is signed"

    def barista_picture(self):
        return f"GomelCoffee barista was draw"


def client_code(factory: Cafe):
    coffee = factory.create_coffee()
    pizza = factory.create_pizza()

    print(f"{coffee.logotype()}")
    print(f"{coffee.barista_picture()}")
    print(f"{pizza.logotype()}\n")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    minsk = MinskCafe()
    client_code(minsk)

    print("Client: Testing client code with the second factory type:")
    gomel = GomelCafe()
    client_code(gomel)
