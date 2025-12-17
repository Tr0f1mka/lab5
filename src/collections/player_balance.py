from collections import UserDict

from src.collections.player_collection import PlayerCollection
from src.logger import logger


class PlayerBalance(UserDict):

    def __setitem__(self, key: str, item: int) -> None:
        """
        Добавление элемента
        :param key: Строка - имя игрока
        :param item: Число - баланс игрока
        """

        if key not in self or self[key] != item:
            logger.info(f"Игрок: {key}, баланс: {item}")
            return super().__setitem__(key, item)


    def sum(self) -> int:
        """
        Сумма балансов игроков
        :return: Число - сумма балансов игроков
        """

        a = 0
        for i in self:
            a += self[i]
        return a


    def update_balance(self, players: PlayerCollection) -> None:
        """
        Обновление балансов
        :param players: Коллекция игроков
        :return: Ничего
        """

        a = list(self.keys())
        for i in players:
            self[i.name] = i.balance
            if i.name in a:
                a.remove(i.name)
        for i in a:
            del self[i]
            logger.info(f"Счёт игрока {i} был удалён")
