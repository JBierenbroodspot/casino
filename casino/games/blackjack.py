from casino.games.cards import DeckOfCards, Hand, CardEnum, CardValue
from casino.games.game import Game
from casino.users.users import User


class BlackjackHand(Hand):
    @property
    def value(self) -> tuple:
        values = [sum(map(int, self.cards))]
        if CardValue.ACE in self.cards:
            if values[0] + 10 < 21:  # Ace is worth either 1 or 11 and its enum value is 1 so 10 is added
                values.append(values[0] + 10)
            if values[0] + 10 == 21:  # No need to return other values if blackjack
                values = [21]
        return tuple(values)


class Blackjack(Game):
    """A game of blackjack
    
    Attributes:
        deck: Instance of DeckOfCards representing the cards the game will be played with.
        player_hand: BlackjackHand representing the cards in the player's hands.
        house_hand: BlackjackHand representing the cards in the house's hands.
        game_ended: Check whether the game has ended.
        player_bet: Float representing the amount of money the player has bet.      
        
    TODO:
        Add User class to game
    """

    def __init__(self, user: User, deck: DeckOfCards):
        super().__init__(user=user)
        self.deck = deck
        self.player_hand = BlackjackHand()
        self.house_hand = BlackjackHand()
        self.game_ended = False
        self.player_bet = 0

    def content(self) -> None:
        super().content()
        self.place_bet()
        self.deal_cards()
        self.player_action()
        input("LOG: End")

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
                        break
                    else:
                        print("You do not have enough balance.")
                        self.end_game()
                except ValueError:
                    print("Please enter a valid value")
                    continue
        return None

    def deal_cards(self) -> None:
        """Deals cards to the user and house, returns None.

        Deals two cards to player and house each. House receives one open and one closed card.
        If cards have already been dealt this method just returns None.

        TODO:
            Drawn cards should be discarded after use.
        """
        self.deck.shuffle_cards()  # This shuffle includes any previously discarded cards.
        if len(self.house_hand.cards) == 0 and len(self.player_hand.cards) == 0:  # Check if cards are already dealt.
            _player_card_1 = self.deck.pick_card(discard=True)
            print(f"Player receives a {_player_card_1}")
            _house_card_1 = self.deck.pick_card(discard=True)
            print(f"House receives a {_house_card_1}")
            _player_card_2 = self.deck.pick_card(discard=True)
            print(f"Player receives a {_player_card_2}")
            _house_card_2 = self.deck.pick_card(discard=True, is_open=False)
            print(f"House receives a {_house_card_2} card")
            self.player_hand.cards.extend((_player_card_1, _player_card_2))
            self.house_hand.cards.extend((_house_card_1, _house_card_2))
            print("")
            print(f"You have: {self.player_hand.cards} totalling to {self.player_hand.value}")
            print(f"The house has: {self.house_hand.cards} totalling to {self.house_hand.value}")

    def player_action(self) -> None:
        action = self.validate_input("Do you want to 1. hit or 2. stand?", ('1', '2'))
        if action:
            if action == '1':
                pass
            elif action == '2':
                pass
