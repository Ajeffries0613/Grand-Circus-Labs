import unittest

class TestPokerGame(unittest.TestCase):

    def test_check_straight(self):
        self.assertEqual(check_straight('S5', 'S6', 'S7'), 7)
        self.assertEqual(check_straight('S6', 'S5', 'S7'), 7)
        self.assertEqual(check_straight('S3', 'SQ', 'SK'), 0)

    def test_check_3ofa_kind(self):
        self.assertEqual(check_3ofa_kind('S9', 'S9', 'S9'), 9)
        self.assertEqual(check_3ofa_kind('S2', 'S4', 'S2'), 0)

    def test_check_royal_flush(self):
        self.assertEqual(check_royal_flush('SA', 'SK', 'SQ'), 14)
        self.assertEqual(check_royal_flush('S10', 'S9', 'S8'), 0)

    def test_play_cards(self):
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S8', 'S9', 'S10'), -1)
        self.assertEqual(play_cards('S7', 'S7', 'S7', 'S5', 'S5', 'S5'), 1)
        self.assertEqual(play_cards('SA', 'SK', 'SQ', 'S5', 'S6', 'S7'), 1)
        self.assertEqual(play_cards('S3', 'SQ', 'SK', 'S10', 'SJ', 'SQ'), 0)

if __name__ == '__main__':
    unittest.main()
