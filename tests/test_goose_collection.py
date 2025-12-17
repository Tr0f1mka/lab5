import unittest
from unittest.mock import patch
from random import seed

from src.collections.goose_collection import GooseCollection
from src.entities.base_classes import Goose, Player


def prepare() -> GooseCollection:
    a = GooseCollection()
    test_goose = Goose("A")
    test_goose1 = Goose("B")
    test_goose2 = Goose("C")
    a.append(test_goose)
    a.append(test_goose1)
    a.append(test_goose2)

    return a


class TestGooseCollection(unittest.TestCase):


    def test_append(self):

        a = GooseCollection()

        self.assertEqual(a.data, [])

        test_goose = Goose("A")
        a.append(test_goose)

        self.assertEqual(a.data, [test_goose])


    def test_len(self):

        a = GooseCollection()

        self.assertEqual(len(a), 0)

        test_goose = Goose("A")
        a.append(test_goose)
        a.append(test_goose)

        self.assertEqual(len(a), 2)


    @patch("src.collections.goose_collection.logger.info")
    def test_remove(self, mock_logger):

        a = prepare()

        a.remove(a[0])
        self.assertEqual(len(a), 2)
        mock_logger.assert_called_once()


    @patch("src.collections.goose_collection.logger.info")
    def test_get_item(self, mock_logger):

        a = prepare()
        test_goose = Goose("A")
        a.append(test_goose)

        self.assertEqual(a[0], test_goose)

        test_goose1 = Goose("B")
        test_goose2 = Goose("C")
        a.append(test_goose1)
        a.append(test_goose2)
        expect_collection = [test_goose, test_goose1]

        self.assertEqual(a[:2], expect_collection)


    @patch("src.collections.goose_collection.logger.info")
    def test_target(self, mock_logger):

        a = prepare()
        victim = Player("Oleg")
        a.set_target(victim)

        for i in a:
            self.assertEqual(i.target, victim)

        a.set_target()

        for i in a:
            self.assertEqual(i.target, None)


    @patch("src.collections.goose_collection.logger.info")
    def test_random(self, mock_logger):

        seed(1)
        a = prepare()

        self.assertEqual(a.random(), a[0])


    def test_iter(self):                            # Если честно, не совсем уверен, что это так проверяется, поэтому буду благодарен, если напишите в issue, корректно это или нет

        a = prepare()

        self.assertEqual(list(a), a.data)
