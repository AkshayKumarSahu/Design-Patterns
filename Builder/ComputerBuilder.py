from abc import ABC, abstractmethod
class ComputerBuilder(ABC):

    @abstractmethod
    def set_cpu(self):
        pass

    @abstractmethod
    def set_gpu(self):
        pass

    @abstractmethod
    def set_ram(self):
        pass

    @abstractmethod
    def set_storage(self):
        pass

    @abstractmethod
    def build(self):
        pass
