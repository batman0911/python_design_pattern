from observer.Display import MobileDisplay, WebDisplay
from observer.Weather import WeatherData
from observer.WeatherState import WeatherState

if __name__ == "__main__":
    weather_data = WeatherData()
    mobile_display = MobileDisplay()
    web_display = WebDisplay()

    weather_data.attach(mobile_display)
    weather_data.attach(web_display)

    weather_data.set_measurements(WeatherState(15.0, 81.2, 0.9))

