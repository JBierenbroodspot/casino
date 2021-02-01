from casino.games.cards import DeckOfCards, Hand, CardValue, CardEnum
from casino.games.game import Game
from casino.users.users import BaseUser, PlayableUser


class BaseBlackjackPlayer(BaseUser):
    """Base for both playable blackjack player and the house."""
    def __init__(self, username: str):
        super(BaseBlackjackPlayer, self).__init__(username=username)
        self.hand = BlackjackHand()


class BlackjackPlayer(PlayableUser, BaseBlackjackPlayer):
    """A playable character for blackjack.

    Attributes:
        username: Name of the user.
        balance: Amount of money the player has.
    """
    def __init__(self, username: str, balance: float = 100):
        super(BlackjackPlayer, self).__init__(username=username, balance=balance)
        self.bet = 0

    @property
    def bet(self) -> float:
        return self.__bet

    @bet.setter
    def bet(self, amount: float) -> None:
        """Sets the bet property, returns bool.

        Args:
            amount: Amount the player wishes to bet

        Returns:
            Returns True if bet was successful, False if bet amount exceeds balance.
        """
        if amount <= self.balance:
            self.__bet = amount
        else:
            raise ValueError("Amount exceeds balance.")


class BlackjackHand(Hand):
    """Overwrites the value property of Hand.

    Changes the value property of Hand to return multiple values if there is an ace in the hand.
    """
    @property
    def value(self) -> tuple:
        count = 0
        for card in self.cards:
            if int(card) in (11, 12, 13):
                count += 10
            else:
                count += int(card)
        values = [count]
        if CardValue.ACE in [card.value for card in self.cards]:
            if values[0] + 10 < 21:  # Ace is worth either 1 or 11 and its enum value is 1 so 10 is added
                values.append(values[0] + 10)
            if values[0] + 10 == 21:  # No need to return other values if blackjack
                values = [21]
        if max(values) > 21 >= min(values):
            values = [min(values)]
        return tuple(values)


class Blackjack(Game):
    """A game of blackjack
    
    Attributes:
        user: The user currently playing the game.
        deck: Instance of DeckOfCards representing the cards the game will be played with.
        house: BaseBlackjackPlayer representing the house.
        has_game_ending_hand: Is true if there are any game ending hands in the game.
    """

    def __init__(self, user: BlackjackPlayer, deck: DeckOfCards):
        super(Blackjack, self).__init__(user=user)
        self.user = user  # overwrite Game.user to make it of type BlackjackPlayer
        self.deck = deck
        self.house = BaseBlackjackPlayer("House")
        self.has_game_ending_hand = False

    def content(self) -> None:
        super(Blackjack, self).content()
        self.reset_game()
        self.get_player_bet()
        self.first_deal()
        if not self.get_game_ending_hands():
            self.get_player_action()
            self.house_deal()
            self.get_winner()
        self.round_end()

    def reset_game(self) -> None:
        """Resets all the variables in the beginning of a round, returns None."""
        self.has_game_ending_hand = False
        self.user.hand.cards = []
        self.house.hand.cards = []
        self.deck.shuffle_cards()  # This shuffle includes any previously discarded cards.
        print(len(self.deck.cards))

    def get_player_bet(self) -> None:
        """Allows user to place bets, returns None."""
        print("Please enter the amount you want to bet.")
        while self.user.bet == 0:
            input_ = input(">>> ")
            try:
                input_ = float(input_)
                self.user.bet = input_
            except ValueError as e:
                print(str(e))
                continue

    def first_deal(self) -> None:
        """Deals cards to the user and house, returns None.

        Deals two cards to player and house each. House receives one open and one closed card.
        If cards have already been dealt this method just returns None.
        """
        if len(self.house.hand.cards) == 0 and len(self.user.hand.cards) == 0:  # Check if cards are already dealt.
            print(self.deal_card(self.user))
            print(self.deal_card(self.house))
            print(self.deal_card(self.user))
            print(self.deal_card(self.house, is_open=False))
            print(f"The house has: {self.house.hand.cards} totalling to {self.house.hand.value}")

    def deal_card(self, player: BaseBlackjackPlayer, is_open: bool = True) -> str:
        """Picks card from top of the deck and adds it to specified hand, returns string.

        Args:
            player: Receiver of card.
            is_open: Check if card should be dealt open or closed.

        Returns:
            String in format {name} received {card}.
        """
        card = self.deck.pick_card(discard=True, is_open=is_open)
        player.hand.cards.append(card)
        return f"\n{player.username} received {card}. Total is: {player.hand.value}"

    def house_deal(self) -> None:
        """Deals cards to house, returns None

        Deals cards to house adhering to the following rules:
            - House stops at soft 17 or above
        """
        if not self.has_game_ending_hand:
            while max(self.house.hand.value) < 17:
                print(f"{self.deal_card(self.house)}")

    def get_player_action(self) -> None:
        """Asks the user which blackjack action they want to use, returns None.

        Asks the player what they wants to do and then executes the corresponding method.

        TODO:
            Add double down action
            Add split action
        """
        print(f"\nYou have: {self.user.hand.cards} totalling to {self.user.hand.value}")
        while not self.get_game_ending_hands():
            action = self.validate_input("Do you want to 1. hit or 2. stand?", ('1', '2'))
            if action == '1':
                self.action_hit()
            elif action == '2':
                self.action_stand()
                break

    def get_winner(self) -> None:
        """Happens when all cards are dealt and no one has a blackjack or is bust."""
        if not self.get_game_ending_hands():
            if max(self.user.hand.value) > max(self.house.hand.value):  # Values above 21 are omitted
                self.event_player_wins()
            elif max(self.user.hand.value) == max(self.house.hand.value):
                self.event_player_push()
            else:
                self.event_house_wins()

    def get_game_ending_hands(self) -> bool:
        """Checks for the different kinds of hands the player and house has, returns bool.

        Returns:
            True if there are any game-ending hands, false if the game continues as usually.
            Game ending hands are if someone has either blackjack or has gone bust.
        """
        end = False
        if 10 in self.house.hand.value:  # Check if house's first card is a 10
            if self.action_peek_cards() == 1:  # Peek the card to check for and ace. CardValue.ACE has a value of 1
                self.event_house_blackjack()
                end = True
        elif 11 in self.house.hand.value:  # Check if house's first card is an ace
            if self.action_peek_cards() in (10, 11, 12, 13):  # TEN, JACK, QUEEN, KING in respective order
                self.event_house_blackjack()
                end = True
        elif min(self.house.hand.value) > 21:  # Check if house has gone bust
            self.event_house_bust()
            end = True
        elif max(self.user.hand.value) == 21:  # Check for player blackjack
            self.event_player_blackjack()
            end = True
        elif min(self.user.hand.value) > 21:  # Check if player has gone bust
            self.event_player_bust()
            end = True
        self.has_game_ending_hand = end
        return end

    def round_end(self) -> None:
        """Asks user if the game should be ended or not, returns None."""
        input_ = self.validate_input("\nDo you want to play another round?[y/n]", ("y", "n"))
        if input_ == "n":
            self.has_ended = True
        else:
            self.user.bet = 0

    def action_hit(self) -> None:
        """Activates when user chooses hit, returns None."""
        print(self.deal_card(self.user))

    def action_stand(self) -> None:
        """Activates when user chooses to stand, returns None."""
        self.action_house_reveal()

    def action_house_reveal(self) -> None:
        """Reveals cards in house_hand, returns None."""
        self.house.hand.reveal_hand()
        print(f"\nThe house reveals their hand containing: {self.house.hand}, totalling to {self.house.hand.value}")

    def action_peek_cards(self) -> int:
        """Gets the value of a closed card, returns int."""
        for card in self.house.hand.cards:
            if not card.is_open:
                return int(card.value)

    def event_house_blackjack(self) -> None:
        """Event for when house has blackjack, returns None."""
        if 21 in self.user.hand.value:
            self.event_player_push()
        else:
            print("The house has blackjack")
            self.event_house_wins()

    def event_player_blackjack(self) -> None:
        """Event for when user has blackjack, returns None."""
        win_amount = self.user.bet + 1.5
        print("Congratulations, you win:", win_amount)
        self.user.win_balance(win_amount)

    def event_player_wins(self) -> None:
        """Event for when user wins, returns None."""
        win_amount = self.user.bet
        print("Congratulations, you win:", win_amount)
        self.user.win_balance(self.user.bet)

    def event_house_wins(self) -> None:
        """Event for when house wins, returns None."""
        print("You lose")
        self.user.lose_balance(self.user.bet)

    def event_player_push(self) -> None:
        """Event for when player and house have the same value hand, returns None."""
        print(f"You got a push, your bet of {self.user.bet} is returned")

    def event_house_bust(self) -> None:
        """Event for when house goes bust, returns None."""
        print(f"The house's hand contains {min(self.house.hand.value)}, they're bust")
        self.event_player_wins()

    def event_player_bust(self) -> None:
        """Event for when player goes bust, returns None."""
        print(f"Your hand contains {min(self.user.hand.value)}, you're bust")
        self.event_house_wins()
