from Observer2.Subject.Subject import Subject


class WeatherConcreteSubject(Subject):


    observers = []

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)
