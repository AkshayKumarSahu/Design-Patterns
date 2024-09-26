from tkinter.constants import DISABLED

from Observer.Observers.Display import Display
from Observer.Observers.Zomato import Zomato
from Observer.Subject.WeatherStation import WeatherStation

if __name__ == '__main__':
    ws = WeatherStation()

    obs1 = Zomato
    obs2 = Display

    obs1.register_subjetc(ws)
    obs2.register_subjetc(ws)


    ws.updateWeather(10,50)
