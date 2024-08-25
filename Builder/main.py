from GamingComputerBuilder import GamingComputerBuilder
from WorkComputerBuilder import WorkComputerBuilder
from ComputerDirector import ComputerDirector

if __name__ == '__main__':
    gb = GamingComputerBuilder()
    director = ComputerDirector(gb)
    director.construct()
    computer1 = director.get_computer()
    print(computer1)

    # work = WorkComputerBuilder()
    # director = ComputerDirector(work)
    # director.construct()
    # computer2 = director.get_computer()
    # print(computer2)

