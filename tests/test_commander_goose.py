import unittest
from unittest.mock import patch

from src.entities.geese import CommanderGoose
from src.entities.base_classes import Goose, Player, GooseCollection


class TestCommanderGoose(unittest.TestCase):

    @patch("src.entities.geese.print")
    def test_target(self, mock_print):

        geese = GooseCollection()
        for i in "ABC":
            test_goose = Goose(i)
            geese.append(test_goose)
        test_commander = CommanderGoose("D")
        geese.append(test_commander)
        test_player = Player("A")

        geese[-1].target_on_player(test_player, geese)

        for i in geese:
            self.assertEqual(i.target, test_player)
