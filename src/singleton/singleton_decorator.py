""" Intent:
Singleton is a creational design pattern that lets you ensure that a class has
only one instance, while providing a global access point to this instance.
"""


def singleton(class_):
    instances = {}

    def get_instances(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instances


@singleton
class Singleton:
    def __init__(self, my_str: str):
        self.my_str = my_str

    def some_business_logic(self):
        pass


if __name__ == "__main__":
    s1 = Singleton("s1 str")
    s2 = Singleton("s2 str")

    assert id(s1) == id(s2), "The instances not the same"

    print(s1.__dict__)  # {'my_str': 's1 str'}
    print(s2.__dict__)  # {'my_str': 's1 str'}
    # The instances the same, because of singleton.
