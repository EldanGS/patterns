"""Intent
Decorator is a structural pattern that allows adding new behaviors to objects
dynamically by placing them inside special wrapper objects.
"""

from abc import ABC, abstractmethod


class Beverage(ABC):
    description = "Unknown Beverage"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass


class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self):
        pass


# Implementation of coffees in the below #
class Espresso(Beverage):
    description = "Espresso"

    def get_description(self):
        return self.description

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    description = "House Blend Coffee"

    def get_description(self):
        return self.description

    def cost(self) -> float:
        return 0.89


class DarkRoast(Beverage):
    description = "Dark Roast"

    def get_description(self):
        return self.description

    def cost(self) -> float:
        return 0.99


class Decaf(Beverage):
    description = "Decaf"

    def get_description(self):
        return self.description

    def cost(self) -> float:
        return 1.05


# Implementation of condiments decorators in the below #
class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return 0.20 + self.beverage.cost()


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self) -> float:
        return 0.15 + self.beverage.cost()


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return 0.10 + self.beverage.cost()


if __name__ == "__main__":
    beverage = Espresso()
    print(f"{beverage.get_description()}, cost: ${beverage.cost()}")

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"{beverage2.get_description()}, cost: ${beverage2.cost()}")

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"{beverage3.get_description()}, cost: ${beverage3.cost()}")
