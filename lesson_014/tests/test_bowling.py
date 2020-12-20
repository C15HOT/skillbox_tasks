import unittest

from bowling import Game, get_score


class ChildTest(unittest.TestCase):

    def setUp(self):
        self.game1 = Game()
        self.game2 = Game()
        self.game3 = Game()
        self.game4 = Game()
        self.get_score = get_score

    def test_equal(self):
        results = ['3532X332/3/62--XX',
                   '5511X332/3/62--XX',
                    ]
        self.get_score(self.game1, results[0])
        self.assertEqual(self.game1.score, 117)
        self.get_score(self.game2, results[1])
        self.assertEqual(self.game2.score, 116)

    def test_exception(self):
        results = ['532332/3/62--62X', '3532X332/3/62--XXX']
        with self.assertRaises(ValueError):
            self.get_score(self.game4, results[0])
        with self.assertRaises(ValueError):
            self.get_score(self.game4, results[1])

if __name__ == '__main__':
    unittest.main()