from typing import TYPE_CHECKING, overload, SupportsIndex, Iterator
from random import choice

if TYPE_CHECKING:
    from src.entities.base_classes import Goose, Player
from src.logger import logger


class GooseCollection():
    """
    Коллекция гусей
    """

    def __init__(self) -> None:
        """
        Инициализация коллекции
        :return: Ничего
        """

        self.data: list["Goose"] = []


    def append(self, goose: "Goose") -> None:
        """
        Добавление игрока
        :param goose: Новый гусь
        :return: Ничего
        """

        self.data.append(goose)


    def __len__(self) -> int:
        """
        Вычисляет длину коллекции
        :return: Число - длина коллекции
        """

        return len(self.data)


    def remove(self, goose: "Goose") -> None:
        """
        Удаление гуся из коллекции
        :param goose: Гусь - удаляемый элемент
        :return: Ничего
        """

        logger.info(f"Удалён гусь {goose.name}")
        self.data.remove(goose)

    @overload
    def __getitem__(self, index: SupportsIndex) -> "Goose":
        ...

    @overload
    def __getitem__(self, index: slice) -> "GooseCollection":
        ...


    def __getitem__(self, key: SupportsIndex | slice) -> "Goose | GooseCollection":
        """
        Открывает доступ по индексам и срезы
        :param key: Число(индекс) или срез
        :return: Гусь или коллекция гусей(срезанная)
        """

        if key is slice:
            return GooseCollection(self.data[key])           #type: ignore
        return self.data[key]                                #type: ignore


    def __iter__(self) -> Iterator:
        """
        Дарует коллекции способность итерироваться
        :return: Итератор
        """

        return iter(self.data)


    def set_target(self, target: "Player | None" = None) -> None:
        """
        Устанавливает цель для всех гусей
        :param target: Игрок или ничего - общая цель гусей
        :return: Ничего
        """

        for i in self:
            i.target = target


    def random(self) -> "Goose":
        """
        Случайный элемент
        :return: Гусь - случайный гусь коллекции
        """

        return choice(self.data)
