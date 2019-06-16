
class player(object):
    """
    This class contains the framework for the player.
    Both robots and human players use this framework.
    """

    def __init__(self, credits, user_name, type, strategy):
        self.credits = credits
        self.user_name = user_name
        self.hand = []
        self.type = type
        self.strategy = strategy

    def get_player_action(self):

        if self.type == 'robot':
            return self.strategy.action()

        player_options = {
            '1': 'raise',
            '2': 'check',
            '3': 'fold',
            '4': 'call'
        }
        if self.type == 'human':
            print(
                'Please choose one of the four options.\n'
                '1. Raise\n'
                '2. Check\n'
                '3. Fold\n'
                '4. Call'
            )
            return player_options[input('Choice:')]
