from collections import UserDict

from src.collections.goose_collection import GooseCollection
from src.logger import logger


class GooseBalance(UserDict):

    def __setitem__(self, key: str, item: int) -> None:
        """
        Добавление элемента
        :param key: Строка - имя гусей
        :param item: Число - баланс гусей
        :return: Ничего
        """

        if key not in self or self[key] != item:
            logger.info(f"Гусь {key}, баланс: {item}")
            return super().__setitem__(key, item)


    def sum(self) -> int:
        """
        Сумма балансов гусей
        :return: Число - сумма балансов гусей
        """

        a = 0
        for i in self:
            a += self[i]
        return a


    def update_balance(self, geese: GooseCollection) -> None:
        """
        Обновление балансов
        :param geese: Коллекция гусей
        :return: Ничего
        """

        a = list(self.keys())
        for i in geese:
            self[i.name] = i.balance
            if i.name in a:
                a.remove(i.name)
        for i in a:
            del self[i]
            logger.info(f"Счёт гуся {i} был удалён")
