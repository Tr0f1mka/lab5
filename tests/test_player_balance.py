import unittest
from unittest.mock import patch

from src.collections.player_balance import PlayerBalance, PlayerCollection
from src.entities.base_classes import Player


class TestPlayerBalance(unittest.TestCase):

    @patch("src.collections.player_balance.logger.info")
    def test_set_item(self, mock_logger):

        a = PlayerBalance()

        self.assertEqual(len(a), 0)
        a["Test Player"] = 23
        self.assertEqual(len(a), 1)
        mock_logger.assert_called_once()

        a["Test Player"] = 23
        self.assertEqual(len(a), 1)
        mock_logger.assert_called_once()


    @patch("src.collections.player_balance.logger.info")
    def test_sum(self, mock_logger):

        a = PlayerBalance()

        self.assertEqual(a.sum(), 0)
        a["A"] = 23
        self.assertEqual(a.sum(), 23)
        a["B"] = 45
        self.assertEqual(a.sum(), 68)


    @patch("src.collections.player_balance.logger.info")
    def test_update_balance(self, mock_logger):

        a = PlayerBalance()
        b = PlayerCollection()

        a["A"] = 23
        a["B"] = 45
        test_player = Player("C")
        b.append(test_player)

        a.update_balance(b)
        self.assertEqual(a, {"C": 100})
