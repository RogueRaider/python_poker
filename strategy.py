
class simple(object):
    def __init__(self, cards):
        self.cards = cards

    def action(self):
        # raise, call, fold, check
        # these are the four possible options
        return 'check'