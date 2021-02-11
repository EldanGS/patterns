import copy


class Prototype:
    prototype_field = "some field"


def main():
    prototype = Prototype()
    prototype_copy = copy.deepcopy(prototype)

    assert prototype is not prototype_copy, "Something went wrong."
    print(prototype_copy.prototype_field)


if __name__ == "__main__":
    main()
