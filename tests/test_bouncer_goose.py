import unittest
from unittest.mock import patch
from random import seed

from src.entities.geese import BouncerGoose
from src.entities.base_classes import Player, PlayerCollection


class TestBouncerGoose(unittest.TestCase):

    @patch("src.entities.geese.print")
    def test_repress_with_succes(self, mock_print):

        seed(23)
        test_goose = BouncerGoose("A")
        players = PlayerCollection()
        for i in "ABC":
            test_player = Player(i)
            players.append(test_player)

        primer = players[0]

        test_goose.repress(primer, players)

        self.assertEqual(len(players), 2)
        self.assertNotIn(primer, players)


    @patch("src.entities.geese.print")
    def test_repress_with_lose(self, mock_print):

        seed(1)
        test_goose = BouncerGoose("A")
        players = PlayerCollection()
        for i in "ABC":
            test_player = Player(i)
            players.append(test_player)

        primer = players[0]

        test_goose.repress(primer, players)

        self.assertEqual(len(players), 3)
        self.assertIn(primer, players)
