from src.simulation import run_simulation
import typer                   #type: ignore


"""
-------------------------
-------Точка входа-------
-------------------------
"""

app = typer.Typer()


@app.command()
def run(
    x: int = typer.Option(20, "-x", "--steps", help="Количество шагов симуляции"),
    s: int = typer.Option(None, "-s", "--seed", help="Сид симуляции"),
    b: bool = typer.Option(False, "-b", "--big", help="Режим большой игры(больше участников)")
) -> None:
    """
    Запускает симуляцию
    """

    run_simulation(x, s, int(b))


if __name__ == "__main__":
    app()
