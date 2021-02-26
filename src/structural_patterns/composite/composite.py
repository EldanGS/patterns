"""Intent:
Composite is a structural design pattern that lets you compose objects into tree structures and
then work with these structures as if they were individual objects.
"""
from abc import ABC, abstractmethod
from typing import List


class Unit(ABC):
    @abstractmethod
    def show(self):
        raise NotImplementedError("You should implement this!")


class CompositeTeam(Unit):  # Squad
    def __init__(self):
        self.team: List[Unit] = []

    def show(self) -> None:
        for unit in self.team:
            print(unit.show())

    def add(self, unit: Unit):
        self.team.append(unit)

    def remove(self, unit: Unit):
        self.team.remove(unit)


class Archer(Unit):
    def __str__(self):
        return "Archer"

    def __init__(self, id_):
        self.id_ = id_

    def show(self) -> str:
        return f"I'm {str(self)}, id: {self.id_}"


class Knight(Unit):
    def __str__(self):
        return "Knight"

    def __init__(self, id_):
        self.id_ = id_

    def show(self) -> str:
        return f"I'm {str(self)}, id: {self.id_}"


if __name__ == "__main__":
    squad = CompositeTeam()
    squad.add(Knight(1))
    squad.add(Knight(12))
    squad.add(Knight(123))
    squad.add(Archer(333))
    squad.add(Archer(222))
    squad.add(Archer(111))

    print("Squad:")
    print(squad.show())

    big_squad = CompositeTeam()
    big_squad.add(Knight(2))
    big_squad.add(Knight(3))
    big_squad.add(Knight(4))
    big_squad.add(Knight(5))
    big_squad.add(squad)

    print("Big Squad:")
    print(big_squad.show())

    """
    Squad:
    I'm Knight, id: 1
    I'm Knight, id: 12
    I'm Knight, id: 123
    I'm Archer, id: 333
    I'm Archer, id: 222
    I'm Archer, id: 111

    Big Squad:
    I'm Knight, id: 2
    I'm Knight, id: 3
    I'm Knight, id: 4
    I'm Knight, id: 5
    I'm Knight, id: 1
    I'm Knight, id: 12
    I'm Knight, id: 123
    I'm Archer, id: 333
    I'm Archer, id: 222
    I'm Archer, id: 111

    """
