import unittest
from unittest.mock import patch
from random import seed

from src.entities.geese import WarGoose, Player


class TestWarGoose(unittest.TestCase):

    @patch("src.entities.geese.print")
    def test_attack_with_succes_without_target(self, mock_print):

        seed(2)
        test_goose = WarGoose("A")
        test_player = Player("B")

        test_goose.attack(test_player)

        self.assertEqual(test_goose.balance, 27)
        self.assertEqual(test_player.balance, 73)


    @patch("src.entities.geese.print")
    def test_attack_with_lose_without_target(self, mock_print):

        seed(1)
        test_goose = WarGoose("A")
        test_player = Player("B")

        test_goose.attack(test_player)

        self.assertEqual(test_goose.balance, 0)
        self.assertEqual(test_player.balance, 100)


    @patch("src.entities.geese.print")
    def test_attack_with_succes_with_target(self, mock_print):

        seed(2)
        test_goose = WarGoose("A")
        test_player = Player("B")
        test_target = Player("C")
        test_goose.target = test_target

        test_goose.attack(test_player)

        self.assertEqual(test_goose.balance, 27)
        self.assertEqual(test_player.balance, 100)
        self.assertEqual(test_target.balance, 73)


    @patch("src.entities.geese.print")
    def test_attack_with_lose_with_target(self, mock_print):

        seed(1)
        test_goose = WarGoose("A")
        test_player = Player("B")
        test_target = Player("C")
        test_goose.target = test_target

        test_goose.attack(test_player)

        self.assertEqual(test_goose.balance, 0)
        self.assertEqual(test_player.balance, 100)
        self.assertEqual(test_target.balance, 100)
