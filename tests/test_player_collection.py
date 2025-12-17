import unittest
from unittest.mock import patch
from random import seed

from src.collections.player_collection import PlayerCollection
from src.entities.base_classes import Goose, Player


def prepare() -> PlayerCollection:
    a = PlayerCollection()
    test_player = Player("A")
    test_player1 = Player("B")
    test_player2 = Player("C")
    a.append(test_player)
    a.append(test_player1)
    a.append(test_player2)

    return a


class TestPlayerCollection(unittest.TestCase):


    def test_append(self):

        a = PlayerCollection()

        self.assertEqual(a.data, [])

        test_player = Player("A")
        a.append(test_player)

        self.assertEqual(a.data, [test_player])


    def test_len(self):

        a = PlayerCollection()

        self.assertEqual(len(a), 0)

        test_player = Player("A")
        a.append(test_player)
        a.append(test_player)

        self.assertEqual(len(a), 2)


    @patch("src.collections.player_collection.logger.info")
    def test_remove(self, mock_logger):

        a = prepare()

        a.remove(a[0])
        self.assertEqual(len(a), 2)
        mock_logger.assert_called_once()


    @patch("src.collections.player_collection.logger.info")
    def test_get_item(self, mock_logger):

        a = prepare()
        test_player = Player("A")
        a.append(test_player)

        self.assertEqual(a[0], test_player)

        test_player1 = Player("B")
        test_player2 = Player("C")
        a.append(test_player1)
        a.append(test_player2)
        expect_collection = [test_player, test_player1]

        self.assertEqual(a[:2], expect_collection)


    @patch("src.collections.player_collection.logger.info")
    def test_random(self, mock_logger):

        seed(1)
        a = prepare()

        self.assertEqual(a.random(), a[0])


    def test_iter(self):                            # Если честно, не совсем уверен, что это так проверяется, поэтому буду благодарен, если напишите в issue, корректно это или нет

        a = prepare()

        self.assertEqual(list(a), a.data)


    def test_honk_update(self):

        a = prepare()

        a.honk_update()

        for i in a:
            self.assertEqual(i.balance, 95)


    @patch("src.collections.player_collection.print")
    def test_credit_update(self, mock_print):

        a = prepare()

        test_creditor = Goose("A")
        a[0].creditor = test_creditor
        a[0].moves_with_credit = 1
        a[1].creditor = test_creditor
        a[1].moves_with_credit = 2
        a[2].creditor = None
        forest_player = Player("D")
        a.append(forest_player)
        a[3].creditor = test_creditor
        a[3].moves_with_credit = 1
        a[3].balance = 20
        a.update_credit()

        self.assertEqual(a[0].creditor, None)
        self.assertEqual(a[0].moves_with_credit, 0)
        self.assertEqual(a[0].balance, 78)

        self.assertEqual(a[1].creditor, test_creditor)
        self.assertEqual(a[1].moves_with_credit, 1)
        self.assertEqual(a[1].balance, 100)

        self.assertEqual(a[2].creditor, None)
        self.assertEqual(a[2].moves_with_credit, 0)
        self.assertEqual(a[2].balance, 100)

        self.assertTrue(forest_player not in a)


    @patch("src.collections.player_collection.print")
    def test_protect_update(self, mock_print):

        a = prepare()

        a[0].protected = True
        a[0].moves_with_protect = 2
        a[1].protected = True
        a[1].moves_with_protect = 1
        a[2].protected = False
        a.update_protect()

        self.assertTrue(a[0].protected)
        self.assertFalse(a[1].protected)
        self.assertFalse(a[2].protected)

        self.assertEqual(a[0].moves_with_protect, 1)
        self.assertEqual(a[1].moves_with_protect, 0)
        self.assertEqual(a[2].moves_with_protect, 0)
