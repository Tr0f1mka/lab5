import unittest
from unittest.mock import patch
from random import seed

from src.entities.base_classes import Goose, Player, GooseCollection, PlayerCollection
from src.entities.geese import WarGoose, HonkGoose


def test_collects():
    geese = GooseCollection()
    players = PlayerCollection()
    for i in "ABC":
        goose = Goose(i)
        geese.append(goose)
        player = Player(i)
        players.append(player)

    return players, geese


class TestGoose(unittest.TestCase):

    @patch("src.entities.base_classes.print")
    def test_steel_with_succes(self, mock_print):

        seed(5)

        test_goose = Goose("A")
        test_player = Player("A")

        test_goose.steel(test_player)

        self.assertEqual(test_goose.balance, 10)
        self.assertEqual(test_player.balance, 90)


    @patch("src.entities.base_classes.print")
    def test_steel_with_unluck(self, mock_print):

        seed(1)

        test_goose = Goose("A")
        test_player = Player("A")

        test_goose.steel(test_player)

        self.assertEqual(test_goose.balance, 0)
        self.assertEqual(test_player.balance, 100)


    @patch("src.entities.base_classes.Goose.steel")
    @patch("src.entities.base_classes.Goose.honk")
    def test_call_with_base_method(self, mock_honk, mock_steel):

        seed(0)

        players, geese = test_collects()

        geese[0](players, geese)

        mock_steel.assert_called_once()
        mock_honk.assert_not_called()


    @patch("src.entities.base_classes.Goose.steel")
    @patch("src.entities.base_classes.Goose.honk")
    @patch("src.entities.geese.WarGoose.attack")
    def test_call_with_child_method(self, mock_attack, mock_honk, mock_steel):

        seed(2)

        players, geese = test_collects()
        war = WarGoose("D")
        geese.append(war)

        geese[3](players, geese)

        mock_steel.assert_not_called()
        mock_honk.assert_not_called()
        mock_attack.assert_called_once()


    def test_add(self):

        goose1 = HonkGoose("A")
        goose1.balance = 3
        goose2 = WarGoose("B")
        goose2.balance = 2

        res = goose1 + goose2

        self.assertEqual(res.name, "A B")
        self.assertEqual(res.balance, 5)

        self.assertIn("attack", dir(res))
        self.assertIn("super_honk", dir(res))
        self.assertIn("steel", dir(res))
        self.assertIn("honk", dir(res))
