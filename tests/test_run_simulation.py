import unittest
from unittest.mock import patch

from src.simulation import run_simulation


class TestRunSimulation(unittest.TestCase):

    @patch("src.simulation.print")
    @patch("src.simulation.logger.info")
    @patch("src.entities.casino.Casino.registr_goose")
    @patch("src.entities.casino.Casino.registr_player")
    @patch("src.entities.casino.Casino.iteration")
    @patch("src.entities.casino.Casino.result")
    @patch("src.simulation.len")
    def test_simulation_stock(self, mock_len, mock_result, mock_iteration, mock_reg_player, mock_reg_goose, mock_logger, mock_print):

        mock_len.return_value = 1

        run_simulation()

        self.assertTrue(mock_reg_goose.call_count <= 15)
        self.assertTrue(mock_reg_goose.call_count >= 5)
        self.assertTrue(mock_reg_player.call_count <= 15)
        self.assertTrue(mock_reg_player.call_count >= 5)
        self.assertEqual(mock_iteration.call_count, 20)


    @patch("src.simulation.print")
    @patch("src.simulation.logger.info")
    @patch("src.entities.casino.Casino.registr_goose")
    @patch("src.entities.casino.Casino.registr_player")
    @patch("src.entities.casino.Casino.iteration")
    @patch("src.entities.casino.Casino.result")
    @patch("src.simulation.len")
    def test_simulation_custom_steps(self, mock_len, mock_result, mock_iteration, mock_reg_player, mock_reg_goose, mock_logger, mock_print):

        mock_len.return_value = 1

        run_simulation(steps=34)

        self.assertTrue(mock_reg_goose.call_count <= 15)
        self.assertTrue(mock_reg_goose.call_count >= 5)
        self.assertTrue(mock_reg_player.call_count <= 15)
        self.assertTrue(mock_reg_player.call_count >= 5)
        self.assertEqual(mock_iteration.call_count, 34)


    @patch("src.simulation.print")
    @patch("src.simulation.logger.info")
    @patch("src.entities.casino.Casino.registr_goose")
    @patch("src.entities.casino.Casino.registr_player")
    @patch("src.entities.casino.Casino.iteration")
    @patch("src.entities.casino.Casino.result")
    @patch("src.simulation.len")
    def test_simulation_big_game(self, mock_len, mock_result, mock_iteration, mock_reg_player, mock_reg_goose, mock_logger, mock_print):

        mock_len.return_value = 1

        run_simulation(big=1)

        self.assertTrue(mock_reg_goose.call_count <= 30)
        self.assertTrue(mock_reg_goose.call_count >= 20)
        self.assertTrue(mock_reg_player.call_count <= 30)
        self.assertTrue(mock_reg_player.call_count >= 20)
        self.assertEqual(mock_iteration.call_count, 20)
