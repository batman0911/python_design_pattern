from abc import ABC, abstractmethod

from observer.Observer import Observer
from observer.Weather import WeatherState


class Display(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class MobileDisplay(Display, Observer):

    def __init__(self):
        self.__weather_state: WeatherState = None

    def display(self) -> None:
        print(f"[Mobile display] Current conditions, temp: {self.__weather_state.temperature}, "
              f"humidity: {self.__weather_state.humidity}")

    def update(self, weather_state: WeatherState) -> None:
        self.__weather_state = weather_state
        self.display()


class WebDisplay(Display, Observer):

    def __init__(self):
        self.__weather_state: WeatherState = None

    def display(self) -> None:
        print(f"[Web display] Current conditions, temp: {self.__weather_state.temperature}, "
              f"humidity: {self.__weather_state.humidity}, "
              f"pressure: {self.__weather_state.pressure}")

    def update(self, weather_state: WeatherState) -> None:
        self.__weather_state = weather_state
        self.display()

