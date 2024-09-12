from Factory.Archer import Archer
from Factory.Knight import Knight
from Factory.factory import PlayerFactory


class CharacterFactory:
    def create_player(self, player_type):
        if player_type == 'Knight':
            return Knight()
        if player_type == 'Archer':
            return Archer()
