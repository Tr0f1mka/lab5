import unittest
from unittest.mock import patch
from random import seed

from src.entities.base_classes import Goose
from src.entities.players import LuckPlayer


class TestLuckPlayer(unittest.TestCase):

    @patch("src.entities.players.print")
    def test_steel_with_succes(self, mock_print):

        seed(2)
        test_player = LuckPlayer("A")
        test_goose = Goose("A")
        test_goose.balance = 30

        test_player.steel_goose(test_goose)

        self.assertEqual(test_player.balance, 116)
        self.assertEqual(test_goose.balance, 14)


    @patch("src.entities.players.print")
    def test_steel_with_lose(self, mock_print):

        seed(0)
        test_player = LuckPlayer("A")
        test_goose = Goose("A")
        test_goose.balance = 30

        test_player.steel_goose(test_goose)

        self.assertEqual(test_player.balance, 100)
        self.assertEqual(test_goose.balance, 30)
