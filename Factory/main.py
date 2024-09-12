from CharacterFactory import CharacterFactory


def create_player(val_from_player):
    player = CharacterFactory().create_player(val_from_player)
    player.attack()


if __name__ == '__main__':
    create_player("Knight")