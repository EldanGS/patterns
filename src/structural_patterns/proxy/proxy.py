"""Intent
Proxy is a structural design pattern that provides an object that acts as a
substitute for a real service object used by a client.
A proxy receives client requests, does some work (access control, caching, etc.)
and then passes the request to a service object.
"""

from abc import ABC, abstractmethod


class AppInterface(ABC):
    @abstractmethod
    def request(self):
        pass


class MyApp(AppInterface):
    def request(self):
        print("App: Handling request")


class MyAppProxy(AppInterface):
    def __init__(self, my_app: MyApp):
        self._my_app = my_app

    def request(self):
        if self.check_access():
            self._my_app.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request!")

    def log_access(self):
        print("Proxy: Logging the time of request.", end="")


def client_code(app: AppInterface):

    app.request()


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    app = MyApp()
    client_code(app)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = MyAppProxy(app)
    client_code(proxy)
