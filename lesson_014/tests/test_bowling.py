import unittest

from bowling import Game, get_score


class ChildTest(unittest.TestCase):

    def setUp(self):
        self.game1 = Game()
        self.game2 = Game()
        self.game3 = Game()

        self.get_score = get_score

    def test_equal(self):
        result = '3532X332/3/62--XX'
        self.get_score(self.game1, result)
        self.assertEqual(self.game1.score, 117)

    def test_exception(self):
        result = '532332/3/62--62X'
        with self.assertRaises(ValueError):
            self.get_score(self.game2, result)

    def test_double_five(self):
        result = '5511X332/3/62--XX'
        with self.assertRaises(ValueError):
            self.get_score(self.game3, result)


if __name__ == '__main__':
    unittest.main()
