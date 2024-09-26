from Observer.Subject.Subject import Subject


class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self.temperature = 0
        self.humidity = 0

    def updateWeather(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.notify_observer(temperature, humidity)