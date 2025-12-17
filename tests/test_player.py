import unittest
from unittest.mock import patch
from random import seed

from src.entities.base_classes import Goose, Player, GooseCollection, PlayerCollection
from src.entities.players import LuckPlayer


def test_collects():
    geese = GooseCollection()
    players = PlayerCollection()
    for i in "ABC":
        goose = Goose(i)
        geese.append(goose)
        player = Player(i)
        players.append(player)

    return players, geese



class TestPlayer(unittest.TestCase):

    @patch("src.entities.base_classes.print")
    def test_dep_with_jackpot(self, mock_print):

        seed(31)
        players, geese = test_collects()

        players[0].dep()

        self.assertEqual(players[0].balance, 150)


    @patch("src.entities.base_classes.print")
    def test_dep_with_win(self, mock_print):

        seed(1)
        players, geese = test_collects()

        players[0].dep()

        self.assertEqual(players[0].balance, 120)


    @patch("src.entities.base_classes.print")
    def test_dep_with_lose(self, mock_print):

        seed(0)
        players, geese = test_collects()

        players[0].dep()

        self.assertEqual(players[0].balance, 90)


    @patch("src.entities.base_classes.print")
    def test_dep_without_dep(self, mock_print):

        players, geese = test_collects()
        players[0].balance = 9

        players[0].dep()

        self.assertEqual(players[0].balance, 9)


    @patch("src.entities.base_classes.print")
    @patch("src.entities.base_classes.Player.dep")
    @patch("src.entities.players.LuckPlayer.steel_goose")
    def test_call_with_parent(self, mock_steel_goose, mock_dep, mock_print):

        players, geese = test_collects()

        players[0](players, geese)

        mock_dep.assert_called_once()
        mock_steel_goose.assert_not_called()


    @patch("src.entities.base_classes.print")
    @patch("src.entities.base_classes.Player.dep")
    @patch("src.entities.players.LuckPlayer.steel_goose")
    def test_call_with_child_with_dep(self, mock_steel_goose, mock_dep, mock_print):

        seed(1)
        players, geese = test_collects()
        luck = LuckPlayer("D")
        players.append(luck)

        players[-1](players, geese)

        mock_dep.assert_called_once()
        mock_steel_goose.assert_not_called()


    @patch("src.entities.base_classes.print")
    @patch("src.entities.base_classes.Player.dep")
    @patch("src.entities.players.LuckPlayer.steel_goose")
    def test_call_with_child_with_steel_goose(self, mock_steel_goose, mock_dep, mock_print):

        seed(0)
        players, geese = test_collects()
        luck = LuckPlayer("D")
        players.append(luck)

        players[-1](players, geese)

        mock_dep.assert_not_called()
        mock_steel_goose.assert_called_once()
