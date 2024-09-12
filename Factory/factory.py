from abc import ABC, abstractmethod

from Factory.Archer import Archer
from Factory.Knight import Knight


class PlayerFactory(ABC):
    @abstractmethod
    def create_player(self):
        pass



class KnightFactory:
    def create_player(self):
        return Knight()

class ArcherFactory:
    def create_player(self):
        return Archer()
    