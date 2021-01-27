from random import shuffle, randint
from enum import Enum


class CardEnum(Enum):
    def __str__(self) -> str:
        return self.name.lower()

    def __repr__(self) -> str:
        return self.__str__()

    def __int__(self) -> int:
        return self.value


class Suit(CardEnum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4
    JOKER = 5
    

class CardValue(CardEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7 
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    JOKER = 14


class Card:
    """A class to simulate the properties of real life playing deck.
    
    Attributes:
        suit: A Suit instance representing the suit of the card.
        value: A CardValue instance representing the value of the card.
        is_open: Checks whether the card is faced up (open) or faced down (closed/hidden).
    """
    def __init__(self, suit: Suit, value: CardValue, is_open: bool = True):
        self.suit = suit
        self.value = value
        self.is_open = is_open
            
    def __str__(self) -> str:
        if self.is_open:
            if self.suit == Suit.JOKER:
                _str = f"{self.value}"
            else:
                _str = f"{self.value} of {self.suit}"
        else:
            _str = "hidden"
        return _str
    
    def __repr__(self) -> str:
        return self.__str__()

    def __int__(self) -> int:
        return int(self.value) if self.is_open else 0


class Hand:
    """A class to represent an actual hand of cards.

    Attributes:
        cards[Card]: The cards in hand.
    """
    def __init__(self):
        self.cards = []

    def __str__(self) -> str:
        len_cards = len(self.cards)
        if len_cards == 0:
            str_ = "nothing"
        elif len_cards == 1:
            str_ = str(self.cards[0])
        elif len_cards == 2:
            str_ = " and ".join([str(card) for card in self.cards])
        else:
            str_ = ", ".join([str(card) for card in self.cards[:-1]]) + " and " + str(self.cards[-1])
        return str_

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def value(self) -> int:
        """The numerical value of the cards in hand. returns int.

        The numerical value is retrieved from CardEnum.__int__.
        """
        return sum(map(int, self.cards))


class DeckOfCards:
    """A deck of deck containing multiple deck.
    
    Attributes:
        deck[Card]: A list of Card objects contained within the deck.
        discarded_cards[*Card]: A list of Card objects no longer in the active card pool.
        jokers: Checks whether the deck contains joker deck or not.
    """
    def __init__(self, jokers: bool = False):
        self.cards = []
        self.discarded_cards = []
        #  Add normal deck to deck, skip all jokers
        for suit in Suit:
            if suit != Suit.JOKER:
                for value in CardValue:
                    if value != CardValue.JOKER:
                        self.cards.append(Card(suit, value))
        #  Add 2 jokers to deck
        if jokers:
            self.cards.append(Card(Suit.JOKER, CardValue.JOKER))
            self.cards.append(Card(Suit.JOKER, CardValue.JOKER))
        self._deck_length = len(self.cards)
                
    def show_cards(self) -> str:
        """Return a string with the deck in current order."""
        return f'This deck contains {self.cards}'
    
    def shuffle_cards(self, include_discarded: bool = True) -> None:
        """Shuffle the list of deck contained in the deck, return None.
        
        Args:
            include_discarded: Include discarded deck into shuffle thus returning them to deck.
        """
        if include_discarded:
            self.cards.extend(self.discarded_cards)
            self.discarded_cards.clear()
        shuffle(self.cards)
    
    def pick_card(self, discard: bool = False, is_open: bool = True, random: bool = False) -> Card:
        """Pick card from top of the deck (index = 0), return Card.
        
        Args: 
            discard: Remove card from deck into discarded_cards if true, default False.
            is_open: Checks whether the card should be dealt face up (open).
            random: Checks whether a random card should be selected rather than the top one.
        """
        _card = self.cards[randint(0, self._deck_length - 1)] if random is True else self.cards[0]
        if is_open:
            _card.is_open = True
        else:
            _card.is_open = False
        if discard:
            self.discarded_cards.append(_card)
            self.cards.remove(_card)
        return _card
