import unittest
from unittest.mock import patch

from src.entities.geese import BankerGoose, Player


class TestBankerGoose(unittest.TestCase):

    @patch("src.entities.geese.print")
    @patch("src.entities.geese.HonkGoose.steel")
    def test_credit_with_succes(self, mock_steel, mock_print):

        test_goose = BankerGoose("A")
        test_player = Player("B")
        test_goose.balance = 20

        test_goose.credit(test_player)

        self.assertEqual(test_goose.balance, 0)
        self.assertEqual(test_player.balance, 120)
        self.assertEqual(test_player.creditor, test_goose)
        mock_steel.assert_not_called()


    @patch("src.entities.geese.print")
    @patch("src.entities.base_classes.Goose.steel")
    def test_credit_with_low_balance(self, mock_steel, mock_print):

        test_goose = BankerGoose("A")
        test_player = Player("B")
        test_goose.balance = 2

        test_goose.credit(test_player)

        self.assertEqual(test_goose.balance, 2)
        self.assertEqual(test_player.balance, 100)
        self.assertEqual(test_player.creditor, None)
        mock_steel.assert_called_once()


    @patch("src.entities.geese.print")
    @patch("src.entities.base_classes.Goose.steel")
    def test_credit_to_player_with_credit(self, mock_steel, mock_print):

        test_goose = BankerGoose("A")
        test_player = Player("B")
        test_goose.balance = 20
        test_player.creditor = test_goose
        test_player.moves_with_credit = 1

        test_goose.credit(test_player)

        self.assertEqual(test_goose.balance, 20)
        self.assertEqual(test_player.balance, 100)
        self.assertEqual(test_player.creditor, test_goose)
        mock_steel.assert_not_called()
