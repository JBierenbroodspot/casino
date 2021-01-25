from casino.games import cards
from casino.games.game import Game


class Blackjack(Game):
    """A game of blackjack
    
    Attributes:
        deck: Instance of DeckOfCards representing the cards the game will be played with.
        player_score: Integer representing the score of the player.
        house_score: Integer representing the score of the house.
        game_ended: Check whether the game has ended.
        player_bet: Float representing the amount of money the player has bet.      
        
    TODO:
        Add User class to game
    """
    def __init__(self, deck: cards.DeckOfCards):
        super().__init__()
        self.cards = deck
        self.player_score = 0
        self.house_score = 0
        self.game_ended = False
        self.player_bet = 0

    def content(self) -> None:
        super().content()
