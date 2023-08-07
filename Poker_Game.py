import unittest

# Define the functions to be tested

def check_straight(card1, card2, card3):
    cards = sorted([card1, card2, card3], key=lambda card: int(card[1:]))
    if int(cards[0][1:]) + 1 == int(cards[1][1:]) and int(cards[1][1:]) + 1 == int(cards[2][1:]):
        return int(cards[2][1:])
    return 0

def check_3ofa_kind(card1, card2, card3):
    if card1[1:] == card2[1:] == card3[1:]:
        return int(card1[1:])
    return 0

def check_royal_flush(card1, card2, card3):
    straight_value = check_straight(card1, card2, card3)
    if straight_value == 14:
        return 14
    return 0

def play_cards(left1, left2, left3, right1, right2, right3):
    left_straight = check_straight(left1, left2, left3)
    right_straight = check_straight(right1, right2, right3)

    if left_straight and right_straight:
        if left_straight > right_straight:
            return -1
        elif left_straight < right_straight:
            return 1
        return 0

    left_3ofa_kind = check_3ofa_kind(left1, left2, left3)
    right_3ofa_kind = check_3ofa_kind(right1, right2, right3)

    if left_3ofa_kind and right_3ofa_kind:
        if left_3ofa_kind > right_3ofa_kind:
            return -1
        elif left_3ofa_kind < right_3ofa_kind:
            return 1
        return 0

    if left_straight:
        return -1
    if right_straight:
        return 1

    left_royal_flush = check_royal_flush(left1, left2, left3)
    right_royal_flush = check_royal_flush(right1, right2, right3)

    if left_royal_flush and not right_royal_flush:
        return -1
    elif not left_royal_flush and right_royal_flush:
        return 1

    return 0

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
