import unittest
from unittest.mock import patch

from src.collections.goose_balance import GooseBalance, GooseCollection
from src.entities.base_classes import Goose


class TestGooseBalance(unittest.TestCase):

    @patch("src.collections.goose_balance.logger.info")
    def test_set_item(self, mock_logger):

        a = GooseBalance()

        self.assertEqual(len(a), 0)
        a["Test Goose"] = 23
        self.assertEqual(len(a), 1)
        mock_logger.assert_called_once()

        a["Test Goose"] = 23
        self.assertEqual(len(a), 1)
        mock_logger.assert_called_once()


    @patch("src.collections.goose_balance.logger.info")
    def test_sum(self, mock_logger):

        a = GooseBalance()

        self.assertEqual(a.sum(), 0)
        a["A"] = 23
        self.assertEqual(a.sum(), 23)
        a["B"] = 45
        self.assertEqual(a.sum(), 68)


    @patch("src.collections.goose_balance.logger.info")
    def test_update_balance(self, mock_logger):

        a = GooseBalance()
        b = GooseCollection()

        a["A"] = 23
        a["B"] = 45
        test_goose = Goose("C")
        b.append(test_goose)

        a.update_balance(b)
        self.assertEqual(a, {"C": 0})
