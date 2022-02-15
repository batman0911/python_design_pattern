from abc import ABC, abstractmethod

from observer.WeatherState import WeatherState


class Observer(ABC):

    @abstractmethod
    def update(self, weather_state: WeatherState) -> None:
        pass
