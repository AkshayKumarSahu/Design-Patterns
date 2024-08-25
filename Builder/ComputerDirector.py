
class ComputerDirector():
    def __init__(self, ComputerBuilder):
        self.c = ComputerBuilder

    def construct(self):
        self.c.set_cpu(23)
        # self.c.set_gpu(4)
        self.c.set_ram(16)
        self.c.set_storage(1024)

    def get_computer(self):
        return self.c.build()
