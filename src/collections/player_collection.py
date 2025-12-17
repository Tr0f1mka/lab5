from typing import TYPE_CHECKING, overload, SupportsIndex, Iterator
from random import choice

if TYPE_CHECKING:
    from src.entities.base_classes import Player
from src.logger import logger


class PlayerCollection():
    """
    Коллекция игроков
    """

    def __init__(self) -> None:
        """
        Инициализация коллекции
        :return: Ничего
        """

        self.data: list["Player"] = []


    def append(self, player: "Player") -> None:
        """
        Добавление игрока
        :param player: Новый игрок
        :return: Ничего
        """

        self.data.append(player)


    def __len__(self) -> int:
        """
        Вычисляет длину коллекции
        :return: Число - длина коллекции
        """

        return len(self.data)


    def remove(self, player: "Player"):
        """
        Удаление игрока из коллекции
        :param goose: Игрок - удаляемый элемент
        :return: Ничего
        """

        logger.info(f"Удалён игрок {player.name}")
        self.data.remove(player)


    @overload
    def __getitem__(self, index: SupportsIndex) -> "Player":
        ...

    @overload
    def __getitem__(self, index: slice) -> "PlayerCollection":
        ...


    def __getitem__(self, key: SupportsIndex | slice) -> "Player | PlayerCollection":
        """
        Открывает доступ по индексам и срезы
        :param key: Число(индекс) или срез
        :return: Игрок или коллекция игроков(срезанная)
        """

        if key is slice:
            return PlayerCollection(self.data[key])               #type: ignore
        return self.data[key]                                     #type: ignore


    def __iter__(self) -> Iterator:
        """
        Дарует коллекции способность итерироваться
        :return: Итератор
        """

        return iter(self.data)


    def random(self) -> "Player":
        """
        Случайный элемент
        :return: Игрок - случайный игрок коллекции
        """

        return choice(self.data)


    def honk_update(self) -> None:
        """
        Обновляет баланс игроков от крика
        :return: Ничего
        """

        for i in self.data:
            if not i.protected:
                i.balance -= 5

                # Баг 2: отрицательный баланс
                # Было: ничего
                # Стало:
                if i.balance < 0:
                    i.balance = 0
    

    def update_credit(self) -> None:
        """
        Обновление сроков кредита
        :return: Ничего
        """

        for i in self.data:

            if i.creditor:
                i.moves_with_credit -= 1
                if i.moves_with_credit == 0:

                    if i.balance < 22:
                        i.creditor.balance += i.balance
                        print(f"Игрока {i.name} увозит в лес гусь {i.creditor.name} из-за невыплаченного долга")
                        self.remove(i)

                    else:
                        i.balance -= 22
                        i.creditor.balance += 22
                        print(f"Игрок {i.name} выплатил долг гусю {i.creditor.name}")
                        i.creditor = None


    def update_protect(self) -> None:
        """
        Обновляет статус защиты
        :return: Ничего
        """

        for i in self.data:

            if i.protected:
                i.moves_with_protect -= 1
                if i.moves_with_protect == 0:
                    i.protected = False
                    print(f"Защита игрока {i.name} истекла")
