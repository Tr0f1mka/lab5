from random import randint, choice

from src.collections.goose_balance import GooseBalance
from src.collections.player_balance import PlayerBalance
from src.collections.goose_collection import GooseCollection
from src.collections.player_collection import PlayerCollection
from src.entities.base_classes import Goose, Player
from src.entities.geese import WarGoose, HonkGoose, BankerGoose, BouncerGoose, CommanderGoose
from src.entities.players import LuckPlayer, DefenderPlayer
from src.constants import PLAYER_NAMES, GOOSE_NAMES
from src.logger import logger


class Casino():
    """
    Казино. Главный класс симуляции
    """

    honk_steps: int = 0
    target_steps: int = 0

    def __init__(self) -> None:
        """
        Инициализация класса
        :return: Ничего
        """

        self.goose_balance = GooseBalance()
        self.player_balance = PlayerBalance()
        self.geese = GooseCollection()
        self.players = PlayerCollection()


    def registr_player(self) -> None:
        """
        Регистрирует нового игрока
        :return: Ничего
        """

        players_types = [Player, LuckPlayer, DefenderPlayer]
        name = choice(PLAYER_NAMES)
        PLAYER_NAMES.remove(name)
        player: Player = choice(players_types)(name)
        self.players.append(player)
        self.player_balance[name] = player.balance
        logger.info(f"ADD {player.__class__.__name__} {player.name}")


    def registr_goose(self) -> None:
        """
        Регистрирует нового гуся
        :return: Ничего
        """

        goose_types = [Goose, WarGoose, HonkGoose, BankerGoose, BouncerGoose, CommanderGoose]
        # goose_types = [BouncerGoose]
        name = choice(GOOSE_NAMES)
        GOOSE_NAMES.remove(name)
        goose: Goose = choice(goose_types)(name)
        self.geese.append(goose)
        self.goose_balance[name] = 0
        logger.info(f"ADD {goose.__class__.__name__} {goose.name}")


    def result(self) -> None:
        """
        Подсчитывает результат игровой сессии
        :return: Ничего
        """

        geese_score = self.goose_balance.sum()*(len(self.players)//2)
        players_score = self.player_balance.sum()
        if geese_score > players_score:
            print("Гусиное ОПГ победило бедных работяг в казино!")
        elif geese_score == players_score:
            print("Ничья! Никто не победил")
        else:
            print("Игроки победили подлых гусей!")
        print(f"Players score: {players_score}          Geese score: {geese_score}")
        print(f"Осталось игроков: {len(self.players)}")
        print(f"Осталось гусей: {len(self.geese)}")


    def iteration(self) -> None:
        """
        1 шаг симуляции
        :return: Ничего
        """

        # Действие игрока
        player = self.players.random()
        player(self.players, self.geese)

        # Действие гуся
        goose = self.geese.random()
        cnt_call = (len(goose.name.split())-1)//2 + 1
        for i in range(cnt_call):
            result = goose(self.players, self.geese)
            if result == 1:
                self.honk_steps = 4
            elif result == 2:
                self.target_steps = 4

            # Баг 5: попытка выгнать игрока при отсутствии игроков
            # Было: ничего
            # Стало:
            if  not self.players:
                self.goose_balance.update_balance(self.geese)
                self.player_balance.update_balance(self.players)
                return

        # Объединение гусей в стаю(10%)
        if len(self.geese) > 1:
            if randint(1, 10) < 2:
                goose1 = self.geese.random()
                while goose1 == goose:
                    goose1 = self.geese.random()
                res = goose + goose1
                del self.goose_balance[goose.name]
                del self.goose_balance[goose1.name]
                self.geese.append(res)
                self.goose_balance[res.name] = res.balance
                self.geese.remove(goose)
                self.geese.remove(goose1)
                print(f"Гуси {goose.name} и {goose1.name} объединились в стаю!")

        # Обработка долгих эффектов
        if self.honk_steps:
            self.players.honk_update()
            self.honk_steps -= 1

        if self.target_steps:
            self.target_steps -= 1
            if not self.target_steps:
                self.geese.set_target()

        # Обновление балансов
        self.players.update_credit()
        self.players.update_protect()
        self.player_balance.update_balance(self.players)
        self.goose_balance.update_balance(self.geese)