import unittest
from unittest.mock import patch

from src.entities.base_classes import Player
from src.entities.players import DefenderPlayer


class TestDefenderPlayer(unittest.TestCase):

    @patch("src.entities.players.print")
    def test_save_player_with_succes(self, mock_print):

        test_defender = DefenderPlayer("A")
        test_player = Player("B")

        self.assertFalse(test_player.protected)
        self.assertEqual(test_player.moves_with_protect, 0)

        test_defender.save_player(test_player)

        self.assertTrue(test_player.protected)
        self.assertEqual(test_player.moves_with_protect, 3)


    @patch("src.entities.players.print")
    def test_save_player_with_unluck(self, mock_print):

        test_defender = DefenderPlayer("A")
        test_player = Player("B")
        test_player.protected = True
        test_player.moves_with_protect = 2

        test_defender.save_player(test_player)

        self.assertTrue(test_player.protected)
        self.assertEqual(test_player.moves_with_protect, 2)
