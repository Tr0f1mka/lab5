from dataclasses import dataclass
from random import randint, choice
import types
from pygame import mixer      #type: ignore
from time import sleep

from src.collections.goose_collection import GooseCollection
from src.collections.player_collection import PlayerCollection

mixer.init()

@dataclass
class Goose():
    """
    Гусь. Самый обычный
    """

    name: str
    balance: int
    target: "None | Player"
    honk_volume: int = randint(1, 10)
    hooonk = mixer.Sound("src/sounds/honk.mp3")
    hooonk.set_volume(honk_volume/10)


    def __init__(self, name: str, target: "None | Player" = None) -> None:
        """
        Инициализирует гуся
        :param name: Строка - имя гуся
        :param target: Ничего или игрок - цель гуся(по умолчанию ничего)
        :return: Ничего не возвращает
        """

        self.name = name
        self.balance = 0
        self.target = target


    def __add__(self, other: "Goose") -> "Goose":
        """
        Складывает двух гусей, соединяя их методы и параметры
        :param other: Прибавляемый гусь
        :return: Гусь - сумма двух изначальных
        """

        # Создание нового класса - микса двух
        result = self.__class__(name=f"{self.name} {other.name}")

        result.balance = self.balance+other.balance
        result.honk_volume = self.honk_volume+other.honk_volume if self.honk_volume+other.honk_volume <= 10 else 10
        result.target = self.target
        result.hooonk.set_volume(result.honk_volume/10)

        methods = {}

        # Методы первого гуся
        for component in dir(self):

            # Без особых методов и атрибутов
            if component.startswith('__') or not callable(getattr(self, component)):
                continue

            # Без повторов
            if hasattr(Goose, component):
                continue

            # Баг 1: объект "target" не является методом
            # Было: ничего
            # Стало:
            if component == "target":
                continue

            methods[component] = getattr(self, component).__func__

        # Методы второго гуся
        for component in dir(other):

            if component.startswith('__') or not callable(getattr(other, component)):
                continue
            
            if hasattr(Goose, component):
                continue
            
            # Баг 1: объект "target" не является методом
            # Было: ничего
            # Стало:
            if component == "target":
                continue

            methods[component] = getattr(other, component).__func__

        # Привязка методов к result
        for method_name, method_func in methods.items():

            if method_name not in dir(Goose):
                bound_method = types.MethodType(method_func, result)
                setattr(result, method_name, bound_method)

        return result


    def __call__(self, players: PlayerCollection, geese: GooseCollection) -> int:
        """
        Вызывает случайный метод гуся
        :param players: Коллекция игроков
        :param geese: Коллекция гусей
        :return: Число - код метода(для долгих эффектов)
        """

        methods = []
        for attr_name in dir(self):

            if attr_name.startswith('__'):
                continue

            attr = getattr(self, attr_name)
            if callable(attr):
                methods.append((attr_name, attr))

        # Выбираем случайный метод
        player = self.target or players.random()
        method_name, method = choice(methods)
        
        # Обработка методов
        result = 0
        if method_name == "honk":
            method()

        elif method_name == "super_honk":
            method()
            result = 1

        else:
            if not player.protected:
                if method_name in ["steel", "attack"]:
                    method(player)
                elif method_name == "credit":
                    if self.balance >= 20:
                        method(player)
                    else:
                        self.steel(player)
                elif method_name == "repress":
                    method(player, players)
                elif method_name == "target_on_player":
                    result = method(player, geese)

            else:
                print(f"Защита игрока {player.name} не позволяет гусю {self.name} творить беспредел")

        return result


    def steel(self, player: "Player") -> None:
        """
        Кража у игрока
        :param player: Игрок - жертва гуся
        :return: Ничего
        """

        if randint(6, 10) > randint(6+player.defence, 8+player.defence):
            s = randint(5, 15)
            if s > player.balance:
                self.balance += player.balance
                print(f"Гусь {self.name} украл у игрока {player.name} {player.balance} GC!")
                player.balance = 0
            else:
                player.balance -= s
                self.balance += s
                print(f"Гусь {self.name} украл у игрока {player.name} {s} GC!")

        else:
            print(f"Гусь {self.name} безуспешно пытается украсть у игрока {player.name}")


    def honk(self):
        """
        Обычный крик(ничего не делает)
        :return: Ничего
        """

        self.hooonk.play()
        sleep(0.3)


@dataclass
class Player():
    """
    Игрок. Тоже самый обычный
    """

    name: str
    balance: int = 100
    luck: float = 1
    protected: bool = False
    moves_with_protect: int = 0
    defence: int = 0
    moves_with_credit: int = 0
    creditor: Goose | None = None


    def __init__(self, name: str) -> None:
        """
        Инициализирует игрока
        :param name: Строка - имя игрока
        :return: Ничего
        """

        self.name = name


    def __call__(self, players: PlayerCollection, geese: GooseCollection) -> None:
        """
        Вызывает случайный метод игрока
        :param players: Коллекция игроков
        :param geese: Коллекция гусей
        :return: Ничего
        """

        methods = []
        # print(self, dir(self))
        for attr_name in dir(self):

            if attr_name.startswith('__'):
                continue

            # Баг 4: вызов creditor как метода класса
            # Было: ничего
            # Стало:
            if attr_name == "creditor":
                continue

            attr = getattr(self, attr_name)
            if callable(attr):
                methods.append((attr_name, attr))

        # print([i[0] for i in methods], self.creditor)

        # Выбираем случайный метод
        method_name, method = choice(methods)
        if method_name == "dep":
            method()
        elif method_name == "steel_goose":
            method(geese.random())
        else:
            # print(method, method_name)
            method(players.random())


    def dep(self) -> None:
        """
        Игрок играет в казино
        :return: Ничего
        """

        if self.balance < 10:
            print(f"Игрок {self.name} хотел депнуть, но ему нехватает денег")
            return
        self.balance -= 10
        a = randint(0, 100)

        if a < 5:
            self.balance += int(60*self.luck)
            print(f"Игрок {self.name} сорвал джекпот! Он выиграл {int(60*self.luck)} GC")

        elif a < 40:
            self.balance += int(30*self.luck)
            print(f"Игрок {self.name} выиграл {int(30*self.luck)} GC")

        else:
            print(f"Игрок {self.name} депнул, но проиграл")
