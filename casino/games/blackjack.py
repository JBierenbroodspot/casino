from casino.games import cards
from casino.games.game import Game
from casino.users.users import User


class Blackjack(Game):
    """A game of blackjack
    
    Attributes:
        deck: Instance of DeckOfCards representing the cards the game will be played with.
        player_hand: Integer representing the value of the cards in the player's hands.
        house_hand: Integer representing the value of the cards in the player's hands.
        game_ended: Check whether the game has ended.
        player_bet: Float representing the amount of money the player has bet.      
        
    TODO:
        Add User class to game
    """
    def __init__(self, user: User, deck: cards.DeckOfCards):
        super().__init__(user=user)
        self.cards = deck
        self.player_hand = 0
        self.house_hand = 0
        self.game_ended = False
        self.player_bet = 0

    def content(self) -> None:
        super().content()
        self.place_bet()

    def place_bet(self) -> None:
        """Allows user to place bets, returns None."""
        if self.player_bet == 0:  # Check if player has not already placed a bet.
            print("Please enter the amount you want to bet.")
            while True:
                _input = input(">>> ")
                try:
                    _input = float(_input)
                    if _input < self.user.balance:
                        self.player_bet = _input
                    else:
                        print("You do not have enough balance.")
                except ValueError:
                    print("Please enter a valid value")
                    continue

    def deal_cards(self, first: bool = False, last: bool = False) -> None:
        """Deals cards to the user and house, returns None.

        Args:
            first: Checks if this is the first draw of the round.
            last: Checks if this is the last draw of the round.
        """
        pass
