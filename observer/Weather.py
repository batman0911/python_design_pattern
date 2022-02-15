from typing import Set

from observer.Observer import Observer
from observer.Subject import Subject
from observer.WeatherState import WeatherState


class WeatherData(Subject):

    def __init__(self):
        self.__observers: Set[Observer] = set()
        self.__weather_state: WeatherState = None

    def attach(self, observer: Observer) -> None:
        self.__observers.add(observer)

    def detach(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify(self) -> None:
        for observer in self.__observers:
            observer.update(self.__weather_state)

    def measurement_changed(self) -> None:
        self.notify()

    def set_measurements(self, weather_state: WeatherState):
        self.__weather_state = weather_state
        self.measurement_changed()
