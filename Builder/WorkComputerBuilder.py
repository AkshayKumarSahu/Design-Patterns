from abc import ABC

from ComputerBuilder import ComputerBuilder
from Computer import Computer


class WorkComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.storage = 0
        self.ram = 0

    def set_cpu(self):
        self.cpu = cpu

    def set_ram(self):
        self.ram = ram
    def set_gpu(self):
        self.gpu = gpu
    def set_storage(self):
        self.storage = 1024

    def build(self):
        c = Computer()
        c.set_cpu(self.cpu)
        c.set_ram(self.ram)
        c.set_storage(self.storage)
        return c
