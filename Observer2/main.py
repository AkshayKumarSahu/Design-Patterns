from Observer2.Observer.Swiggy import Swiggy
from Observer2.Observer.Zomato import Zomato
from Observer2.Subject.WeatherConcreteSubject import WeatherConcreteSubject

if __name__ == '__main__':

    weather = WeatherConcreteSubject()

    obs1 = Zomato()
    obs2 = Swiggy()

    weather.register(obs1)
    weather.register(obs2)

    weather.notify()

