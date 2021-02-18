""" Intent
Adapter is a structural design pattern,
which allows incompatible objects to collaborate.
"""


class Current:
    def request(self) -> str:
        return "Current: The default target's behavior."


class Old:
    def old_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Current):
    def __init__(self, old_version: Old):
        self.adaptee = old_version

    def request(self) -> str:
        # make reverse string, old-version
        return f"Adapter: (TRANSLATED) {self.adaptee.old_request()[::-1]}"


def client_code(current: Current) -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(current.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    current = Current()
    client_code(current)
    print("\n")

    adaptee = Old()
    print(
        "Client: The Adaptee class has a weird interface. "
        "See, I don't understand it:"
    )
    print(f"Adaptee: {adaptee.old_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)
