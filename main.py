from deck import deck, card
from environment import player, poker_table

def main():

    # defaults are 4 robots and one human for simplicity.
    players = []
    for i in range(1, 4):
        players.append(player(100, 'bot_' + str(i), 'robot'))

    human = player(100, 'human_name', 'human')
    players.append(human)

    vegas_table = poker_table(players, deck())

    vegas_table.start_game()

    print('Dealing flop')
    vegas_table.deal_flop()
    for c in vegas_table.cards_on_table:
        print(c.face + ' of ' + c.suit)
    print()

    print('Dealing turn')
    vegas_table.deal_turn()
    for c in vegas_table.cards_on_table:
        print(c.face + ' of ' + c.suit)
    print()

    print('Dealing river')
    vegas_table.deal_river()
    for c in vegas_table.cards_on_table:
        print(c.face + ' of ' + c.suit)
    print()

    print('Thanks for playing')

main()