from random import shuffle

class deck(object):
    """
    Deck is the all the cards being played with in one game. The number of cards will decrease as cards are drawn from the deck
    """
    standard_52 = {
        'cards': {
            'Ace': 13,
            'King': 12,
            'Queen': 11,
            'Jack': 10,
            '10': 9,
            '9': 8,
            '8': 7,
            '7': 6,
            '6': 5,
            '5': 4,
            '4': 3,
            '3': 2,
            '2': 1,
        },

        'suits': {
            'Spades': 'Black',
            'Hearts': 'Red',
            'Clubs': 'Black',
            'Diamonds': 'Red'
        }
    }

    def __init__(self, deck_type=standard_52):
        self.cards = []
        for suit, color in deck_type['suits'].items():
            for face, value in deck_type['cards'].items():
                self.cards.append(card(value, face, color, suit))
        shuffle(self.cards)
        self.number_of_cards = len(self.cards)

    def draw_top_cards(self, quantity):
        cards = []
        for x in range(1, quantity + 1):
            cards.append(self.cards.pop())
        self.number_of_cards = len(self.cards)
        return cards

class card(object):
    """Card is the smallest unit of play"""
    def __init__(self, value, face, color, suit):
        self.value = value
        self.face = face
        self.color = color
        self.suit = suit