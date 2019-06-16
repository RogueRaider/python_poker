
class player(object):
    def __init__(self, credits, user_name, type):
        self.credits = credits
        self.user_name = user_name
        self.hand = []
        self.type = type


class poker_table(object):
    """
    This class contains the logic of the game.
    It accounts for players and the deck given to it.
    """
    def __init__(self, players, deck):
        self.cards_on_table = []
        self.pot = 0
        self.players = players
        self.deck = deck

    def start_game(self):
        print("\nWelcome to python poker. Best of luck! \n\
The game is Texas Hold'em.")

        self.deal_opening_hand()
        for player in self.players:
            print('Player %s has this hand:' % player.user_name)
            for card in player.hand:
                print(card.face + ' of ' + card.suit)
            print()

    def deal_opening_hand(self):
        for player in self.players:
            player.hand = self.deck.draw_top_cards(2)

    # This is the first three community cards
    def deal_flop(self):
        self.cards_on_table = self.deck.draw_top_cards(3)

    # This is the fourth community card
    def deal_turn(self):
        self.cards_on_table = self.cards_on_table + self.deck.draw_top_cards(1)

    # This is the fifth and final community card
    def deal_river(self):
        self.cards_on_table = self.cards_on_table + self.deck.draw_top_cards(1)
