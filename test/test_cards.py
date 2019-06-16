import unittest
from deck import card

class TestCardsClass(unittest.TestCase):

    def test_card_object(self):
        test_c = card(14, 'Ace', 'Black', 'Spades')
        self.assertEqual(test_c.value, 14)
        self.assertEqual(test_c.face, 'Ace')
        self.assertEqual(test_c.color, 'Black')
        self.assertEqual(test_c.suit, 'Spades')

if __name__ == '__main__':
    unittest.main()