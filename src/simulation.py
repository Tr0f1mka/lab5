import random
from src.entities.casino import Casino
from src.logger import logger

def run_simulation(steps: int = 20, seed: int | None = None, big: int = 0) -> None:
    """
    Проводит симуляцию
    :param steps: Число - количество шагов симуляции
    :param seed: Число - сид казино
    :param big: Число(0 или 1) - режим большой игры(больше игроков и гусей)
    :return: Ничего
    """

    random.seed(seed)

    casino = Casino()

    logger.info("===========================================")
    for i in range(random.randint(5+15*big, 15+15*big)):
        casino.registr_goose()
        casino.registr_player()
    print(f"Участвует {i+1} гусей и игроков")

    for i in range(1, steps+1):
        logger.info(f"--------------------------------------------{i}")
        print(f"Шаг {i}")
        casino.iteration()
        if len(casino.players) == 0:
            break
        print("=================================")

    casino.result()
