from abc import ABC, abstractmethod
from Observer.Subject.Subject import Subject


class Observer(ABC):
    @abstractmethod
    def update(self, temprature, humidity):
        pass

    def register_subjetc(self,observer):
        Subject.register_observer(observer)

    def unregister_subjetc(self,observer):
        Subject.unregister_observer(observer)
