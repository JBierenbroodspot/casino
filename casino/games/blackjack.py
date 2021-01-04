from games import cards


class Blackjack():
    """A game of blackjack
    
    Attributes:
        cards: Cards the game will be played with.
        
    TODO:
        Add User class to game
    """
    def __init__(self, cards: cards.DeckOfCards):
        self.cards = cards