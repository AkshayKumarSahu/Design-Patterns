from abc import ABC, abstractmethod



class Subject(ABC):

    @abstractmethod
    def register(self, observer):
        pass

    def unregister(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass