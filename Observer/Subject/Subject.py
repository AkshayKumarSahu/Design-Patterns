

class Subject:

    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)


    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observer(self, temprature, humidity):
        for i in self.observers:
            i.update(temprature, humidity)



