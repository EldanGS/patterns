"""Intent

Observer is a behavioral design pattern that lets you define a subscription mechanism to
notify multiple objects about any events that happen to the object they’re observing.
"""
from abc import ABC, abstractmethod


# ### INTERFACES ### #
from typing import List, Dict, Set


class Observer(ABC):
    # our observer (aka subscribers) interface
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass


class Subject(ABC):
    # our subject (aka notifier)
    @abstractmethod
    def register_observer(self, o: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, o: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


# ### END INTERFACES ### #


# ### IMPLEMENTATIONS ### #
class WeatherData(Subject):
    def __init__(
        self, temperature: float = 0.0, humidity: float = 0.0, pressure: float = 0.0
    ):
        # private params
        self._observers: Set[Observer] = set()
        self._temperature: float = temperature
        self._humidity: float = humidity
        self._pressure: float = pressure

    # Subject - implementations of notification and subscription functionality
    def register_observer(self, observer: Observer) -> None:
        self._observers.add(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    # end implementation

    # built-in functionality - like old code of WeatherData
    def measurements_changed(self) -> None:
        self.notify_observers()

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if self._temperature == value:
            return
        print(f"WeatherData: temperature set: {value}")
        self._temperature = value

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        if self._humidity == value:
            return
        print(f"WeatherData: humidity set: {value}")
        self._humidity = value

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, value):
        if self._pressure == value:
            return
        print(f"WeatherData: pressure set: {value}")
        self._pressure = value

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurements_changed()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __str__(self):
        return "CurrentConditionsDisplay"

    def __init__(
        self, weather_data: Subject, temperature: float = 0.0, humidity: float = 0.0
    ):
        # private params
        self._temperature: float = temperature
        self._humidity: float = humidity
        self._weather_data: Subject = weather_data
        weather_data.register_observer(self)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if self._temperature == value:
            return
        print(f"WeatherData: temperature set: {value}")
        self._temperature = value

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        if self._humidity == value:
            return
        self._humidity = value

    def update(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current Condition Display!!!")
        print(
            f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity\n"
        )


if __name__ == "__main__":
    # Weather Station
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    print("\n")
    weather_data.set_measurements(82, 70, 29.2)
    print("\n")
    weather_data.set_measurements(78, 90, 29.3)
