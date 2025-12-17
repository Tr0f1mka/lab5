from random import randint

from src.entities.base_classes import Player, Goose


class LuckPlayer(Player):
    """
    Ловкий(везучий) игрок
    """

    luck = 1.2
    defence = -1

    def steel_goose(self, goose: Goose):

        if randint(6, 10) < randint(7, 8):
            s = randint(15, 25)
            goose.balance -= s
            self.balance += s
            print(f"Ловкий игрок {self.name} успешно крадёт у гуся {goose.name} {s} монет")

        else:
            print(f"Ловкий игрок {self.name} безуспешно пытается украсть у гуся {goose.name}")


class DefenderPlayer(Player):
    """
    Защищающийся игрок
    """

    luck = 0.8
    defence = 1

    def save_player(self, player: Player) -> None:
        """
        Даёт защиту игроку(гуси не могут его атаковать 3 хода)
        :param player: Игрок - защищаемый подопечный
        :return: Ничего
        """

        if not player.protected:
            player.protected = True
            player.moves_with_protect = 3
            print(f"Игрок {self.name} решил защитить игрока {player.name} от нападок гусей на 3 хода")

        else:
            print(f"Игрок {self.name} хотел защитить игрока {player.name}, но тот уже был защищён")