from ComputerBuilder import ComputerBuilder
from Computer import Computer
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.storage = 0
        self.ram = 0

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_gpu(self, gpu):
        self.gpu = gpu

    def set_ram(self, ram):
        self.ram = ram
    def set_storage(self, storage):
        self.storage = storage

    def build(self):
        c = Computer()
        c.set_cpu(self.cpu)
        c.set_gpu(self.gpu)
        c.set_ram(self.ram)
        c.set_storage(self.storage)
        return c