import unittest
from unittest.mock import patch

from src.entities.geese import HonkGoose


class TestHonkGoose(unittest.TestCase):

    @patch("src.entities.geese.print")
    @patch("src.entities.geese.HonkGoose.hooonk")
    @patch("time.sleep")
    def test_super_honk(self, mock_sleep, mock_hooonk, mock_print):

        test_goose = HonkGoose("A")

        test_goose.super_honk()

        mock_hooonk.play.assert_called_once()
