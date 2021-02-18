"""
Фабричный метод — это порождающий паттерн проектирования,
который определяет общий интерфейс для создания объектов в суперклассе,
позволяя подклассам изменять тип создаваемых объектов.

"""
from abc import ABC, abstractmethod


class LogisticApp(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def deliver(self) -> str:
        # Вызываем фабричный метод, чтобы получить объект-продукт.
        product = self.factory_method()

        # Далее, работаем с этим продуктом.
        result = (
            f"Creator: The same creator's code has just worked with {product.deliver()}"
        )
        return result


class RoadLogistics(LogisticApp):
    def factory_method(self) -> "Transport":
        return Truck()


class SeaLogistics(LogisticApp):
    def factory_method(self) -> "Transport":
        return Ship()


class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass


class Truck(Transport):
    # Concrete transport
    def deliver(self) -> str:
        return f"Deliver by Truck"


class Ship(Transport):
    # Concrete transport
    def deliver(self) -> str:
        return f"Deliver by Ship"


def client_code(creator: LogisticApp):
    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{creator.deliver()}",
        end="",
    )


if __name__ == "__main__":
    print("App: Launched with the RoadLogistics.")
    road_logistics = RoadLogistics()
    client_code(road_logistics)
    print("\n")

    print("App: Launched with the SeaLogistics.")
    sea_logistics = SeaLogistics()
    client_code(sea_logistics)
