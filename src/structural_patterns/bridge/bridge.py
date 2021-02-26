""" Intent:
Bridge pattern compose objects in tree structure.
It decouples abstraction from implementation.
Here abstraction represents the client from which the objects will be called.
"""
from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def is_enabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @abstractmethod
    def set_volume(self, percent):
        pass

    @abstractmethod
    def get_channel(self):
        pass

    @abstractmethod
    def set_channel(self, iter):
        pass


class Remote:
    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self) -> str:
        response = "disabled"
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()
            response = "enabled"

        return f"Device {str(self._device)}: {response}"

    def volume_down(self):
        self._device.set_volume(self._device.get_volume() - 10)

    def volume_up(self):
        self._device.set_volume(self._device.get_volume() + 10)

    def channel_down(self):
        self._device.set_channel(self._device.get_channel() - 1)

    def channel_up(self):
        self._device.set_channel(self._device.get_channel() + 1)


class AdvancedRemote(Remote):
    def mute(self):
        self._device.set_volume(0)


# Но каждое устройство имеет особую реализацию.
class TV(Device):
    def __str__(self):
        return "TV"

    def __init__(self):
        self.state = False
        self.volume = 0
        self.channel = 1

    def is_enabled(self):
        return self.state

    def enable(self):
        self.state = True

    def disable(self):
        self.state = False

    def get_volume(self) -> int:
        return self.volume

    def set_volume(self, percent):
        self.volume += self.volume * percent

    def get_channel(self) -> int:
        return self.channel

    def set_channel(self, iter):
        self.channel += iter


class Radio(Device):
    def __str__(self):
        return "Radio"

    def __init__(self):
        self.state = True
        self.volume = 10
        self.channel = 100

    def is_enabled(self):
        return self.state

    def enable(self):
        self.state = True

    def disable(self):
        self.state = False

    def get_volume(self) -> int:
        return self.volume

    def set_volume(self, percent):
        self.volume += self.volume * percent

    def get_channel(self) -> int:
        return self.channel

    def set_channel(self, iter):
        self.channel += iter


def client_code(abstraction: Remote):
    """
    За исключением этапа инициализации, когда объект Абстракции связывается с
    определённым объектом Реализации, клиентский код должен зависеть только от
    класса Абстракции. Таким образом, клиентский код может поддерживать любую
    комбинацию абстракции и реализации.

    tv = new Tv()
    remote = new Remote(tv)
    remote.togglePower()

    radio = new Radio()
    remote = new AdvancedRemote(radio)
    """
    print(abstraction.toggle_power())


if __name__ == "__main__":
    """
    Клиентский код должен работать с любой предварительно сконфигурированной
    комбинацией абстракции и реализации.
    """

    tv = TV()  # concrete implementation of TV
    remote = Remote(tv)
    client_code(remote)
    print(remote.__dict__)
    # Device TV: enabled
    # {'_device': <__main__.TV object at 0x7ff31e804130>}

    print("\n")

    radio = Radio()  # concrete implementation of Radio
    remote = AdvancedRemote(radio)
    client_code(remote)
    print(remote.__dict__)
    # {'_device': <__main__.Radio object at 0x7ff31bff3ee0>}
    # Device Radio: disabled
