""" Intent:
Singleton is a creational design pattern that lets you ensure that a class has
only one instance, while providing a global access point to this instance.
"""


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, my_str: str):
        self.my_str = my_str

    def some_business_logic(self):
        """There is should be some logic of singleton"""
        pass


if __name__ == "__main__":
    s1 = Singleton("s1 str")
    s2 = Singleton("s2 str")

    assert id(s1) == id(s2), "The instances not the same"

    print(s1.__dict__)  # {'my_str': 's1 str'}
    print(s2.__dict__)  # {'my_str': 's1 str'}
    # The instances the same, because of singleton.
