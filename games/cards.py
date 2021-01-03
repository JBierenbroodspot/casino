from random import shuffle, randint


class Card(object):
    """
    A class to simulate the properties of real life playing cards
    
    Attributes:
        suit: The suit of the card represented as a string e.g. 'hearts' and 'clubs'.
        value: The numerical value of the card going from 0 (ace) to 13 (king) and 14 (joker).
        value_verbose: A human readable version of 'value' e.g. '5' and 'king'.
        color: The color of the suit.
        is_joker: Checks whether card is a joker or not.
    """
    def __init__(self, suit: str, value: int, value_verbose: str, color: str = None, is_joker: bool = False):
        self.value_verbose = value_verbose
        self.color = None
        self.is_joker = is_joker
        if color:
            self.color = color
        if not is_joker:
            self.suit = suit
            self.value = value
        else:
            self.suit = 'joker'
            self.value = 14
            
    def show(self, color: bool = False) -> str:
        """
        Return string of the card's value and suit
        
        Optional argument color shows color if True
        """
        _return = ''
        if self.is_joker:
            _return = f'{self.value_verbose}'
        elif color:
            _return = f'{self.value_verbose} of {self.suit}, color {self.color}'
        else:
            _return = f'{self.value_verbose} of {self.suit}'
        return _return


class DeckOfCards():
    """A deck of cards containing multiple cards.
    
    Attributes:
        cards[*Card]: A list of Card objects contained within the deck.
        discarded_cards[*Card]: A list of Card objects no longer in the active card pool.
        jokers: Checks whether the deck contains joker cards or not.
    """
    def __init__(self, jokers: bool = False):
        self.cards = []
        self.discarded_cards = []
        self._suits = {
            'hearts': 'red',
            'diamonds': 'red',
            'clubs': 'black',
            'spades': 'black'
        }
        self._values = {
            'ace': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'jack': 11,
            'queen': 12,
            'king': 13
        }
        #  Add normal cards to deck
        for suit, color in self._suits.items():
            for name, value in self._values.items():
                self.cards.append(Card(suit, value, name, color))
        #  Add 2 jokers to deck
        if jokers:
            self.cards.append(Card('joker', 14, 'joker', is_joker=True))
            self.cards.append(Card('joker', 14, 'joker', is_joker=True))
        self._deck_length = len(self.cards)
                
    def show_cards(self) -> str:
        """Return a string with the cards in current order"""
        #  Turn Card object into their human readable selves
        _human_readable = [card.show() for card in self.cards]
        return f'This deck contains {_human_readable}'
    
    def shuffle_cards(self, include_discarded: bool = True) -> None:
        """
        Shuffle the list of cards contained in the deck, return None
        
        Optional argument include_discarded:
        Include discarded cards into shuffle thus returning them to deck
        """
        if include_discarded:
            self.cards.extend(self.discarded_cards)
            self.discarded_cards.clear()
        shuffle(self.cards)
        return None
    
    def pick_random_card(self, discard: bool = False) -> Card:
        """
        Pick a random card from deck, Return Card
        
        Optional argument is_remove:
        Remove card from deck into discarded_cards if true, default False
        """
        _card = self.cards[randint(0, self._deck_length - 1)]
        if discard:
            self.discarded_cards.append(_card)
            self.cards.remove(_card)
        return _card
    
    def pick_top_card(self, discard: bool = False) -> Card:
        """
        Pick card from top of the deck (index = 0), return Card
        
        Optional argument discard: 
        Remove card from deck into discarded_cards if true, default False
        """
        _card = self.cards[0]
        if discard:
            self.discarded_cards.append(_card)
            self.cards.remove(_card)
        return _card
        