from random import randint
from time import sleep
from typing import TYPE_CHECKING

from src.entities.base_classes import Goose, Player
if TYPE_CHECKING:
    from src.collections.goose_collection import GooseCollection
    from src.collections.player_collection import PlayerCollection


class WarGoose(Goose):
    """
    Боевой гусь
    """

    def attack(self, player: Player) -> None:
        """
        Атакует игрока(отнимает больше денег)
        """

        if self.target:
            player = self.target

        if randint(6, 10) > randint(5+player.defence, 7+player.defence):
            s = randint(25, 50)
            if s > player.balance:
                self.balance += player.balance
                print(f"Атака гуся {self.name} отнимает у игрока {player.name} {player.balance} GC!")
                player.balance = 0
            else:
                player.balance -= s
                self.balance += s
                print(f"Атака гуся {self.name} отнимает у игрока {player.name} {s} GC!")

        else:
            print(f"Гусь {self.name} безуспешно пытается атаковать игрока {player.name}")



class HonkGoose(Goose):
    """
    Кричащий гусь
    """

    honk_volume = 10

    def super_honk(self) -> None:
        """
        Супер-крик
        :return: Ничего
        """

        print(f"Супер-крик гуся {self.name} заставляет всех игроков терять монеты!")
        self.hooonk.play()
        sleep(0.3)



class BankerGoose(Goose):
    """
    Гусь-кредитор
    """

    def credit(self, player: Player) -> None:
        """
        Выдаёт кредит игроку
        :param player: Игрок, которому дают кредит
        :return: Ничего
        """

        if self.balance >= 20:
            if not player.moves_with_credit:
                player.balance += 20
                self.balance -= 20
                player.moves_with_credit = 5
                player.creditor = self
                print(f"Гусь {self.name} даёт игроку {player.name} в долг 20 GC на 4 хода")

            else:
                print(f"Гусь {self.name} хотел дать денег в долг игроку {player.name}, но тот уже был должен")

        else:
            self.steel(player)



class CommanderGoose(Goose):
    """
    Гусь-командир
    """

    def target_on_player(self, player: Player, geese: "GooseCollection") -> int:
        """
        Устанавливает цель для гусей(все гуси атакуют одного игрока)
        :param player: Игрок - цель гусей
        :param geese: Коллекция гусей
        :return: Число - установлена цель или нет
        """

        if self.target:
            return 0

        geese.set_target(player)
        print(f"Гусь {self.name} даёт команду гусям атаковать игрока {player.name} в течение 4 ходов")
        return 2



class BouncerGoose(Goose):
    """
    Гусь-вышибала
    """

    def repress(self, player: "Player", players: "PlayerCollection") -> None:
        """
        Выгоняет случайного игрока
        :param player: Игрок, подвергающийся репрессии
        :param players: Коллекция игроков
        :return: Ничего
        """

        if player in players:
            if randint(6, 10) > randint(7, 8):
                print(f"Гусю {self.name} не понравился игрок {player.name}, поэтому он его выгнал, забрав деньги")
                self.balance += player.balance
                players.remove(player)
            else:
                print(f"Гусю {self.name} не понравился игрок {player.name}, но ничего с этим поделать не может")
