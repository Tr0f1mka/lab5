import unittest
from unittest.mock import patch

from src.entities.casino import Casino, PLAYER_NAMES, GOOSE_NAMES


class TestCasino(unittest.TestCase):

    @patch("src.entities.casino.logger.info")
    def test_registr_player(self, mock_logger):

        cas = Casino()

        self.assertEqual(len(cas.players), 0)
        self.assertEqual(len(PLAYER_NAMES), 50)

        cas.registr_player()
        self.assertEqual(len(cas.players), 1)
        self.assertEqual(len(PLAYER_NAMES), 49)

        cas.registr_player()
        self.assertEqual(len(cas.players), 2)
        self.assertEqual(len(PLAYER_NAMES), 48)


    @patch("src.entities.casino.logger.info")
    def test_registr_goose(self, mock_logger):

        cas = Casino()

        self.assertEqual(len(cas.geese), 0)
        self.assertEqual(len(GOOSE_NAMES), 79)

        cas.registr_goose()
        self.assertEqual(len(cas.geese), 1)
        self.assertEqual(len(GOOSE_NAMES), 78)

        cas.registr_goose()
        self.assertEqual(len(cas.geese), 2)
        self.assertEqual(len(GOOSE_NAMES), 77)
