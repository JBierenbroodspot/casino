from random import shuffle, randint
from enum import Enum


class Suit(Enum):
    def __str__(self) -> str:
        return self.name.lower()
    
    def __repr__(self) -> str:
        return self.__str__()
    
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4
    JOKER = 5
    

class CardValue(Enum):
    def __str__(self) -> str:
        return self.name.lower()
    
    def __repr__(self) -> str:
        return self.__str__()
    
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
    """A class to simulate the properties of real life playing deck
    
    Attributes:
        suit: A Suit instance representing the suit of the card.
        value: A CardValue instace representing the value of the card.
    """
    def __init__(self, suit: Suit, value: CardValue):
        self.suit = suit
        self.value = value
            
    def __str__(self) -> str:
        if self.suit == Suit.JOKER:
            _str = f"{self.value}"
        else:
            _str = f"{self.value} of {self.suit}"
        return _str
    
    def __repr__(self) -> str:
        return self.__str__()


class DeckOfCards:
    """A deck of deck containing multiple deck.
    
    Attributes:
        deck[Card]: A list of Card objects contained within the deck.
        discarded_cards[*Card]: A list of Card objects no longer in the active card pool.
        jokers: Checks whether the deck contains joker deck or not.
    """
    def __init__(self, jokers: bool=False):
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
        """Return a string with the deck in current order"""
        return f'This deck contains {self.cards}'
    
    def shuffle_cards(self, include_discarded: bool = True) -> None:
        """Shuffle the list of deck contained in the deck, return None
        
        Args:
            include_discarded: Include discarded deck into shuffle thus returning them to deck
        """
        if include_discarded:
            self.cards.extend(self.discarded_cards)
            self.discarded_cards.clear()
        shuffle(self.cards)
        return None
    
    def pick_random_card(self, discard: bool = False) -> Card:
        """ Pick a random card from deck, Return Card
        
        Args:
            discard: Remove card from deck into discarded_cards if true, default False
        """
        _card = self.cards[randint(0, self._deck_length - 1)]
        if discard:
            self.discarded_cards.append(_card)
            self.cards.remove(_card)
        return _card
    
    def pick_top_card(self, discard: bool = False) -> Card:
        """Pick card from top of the deck (index = 0), return Card
        
        Args: 
            Remove card from deck into discarded_cards if true, default False
        """
        _card = self.cards[0]
        if discard:
            self.discarded_cards.append(_card)
            self.cards.remove(_card)
        return _card
