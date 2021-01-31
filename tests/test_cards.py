from casino.games import cards

print("\n# ---------------------------------------- Test Suit ---------------------------------------- #\n")
for suit in cards.Suit:
    print(f"Suit.__repr__: {suit.__repr__()}, Suit.__int__: {suit.__int__()}")
print("\n# ---------------------------------------- Test CardValue ---------------------------------------- #\n")
for val in cards.CardValue:
    print(f"Suit.__repr__: {val.__repr__()}, Suit.__int__: {val.__int__()}")
print("\n# ---------------------------------------- Test Card ---------------------------------------- #\n")
all_cards_open = []  # A list of all possible card combinations
all_cards_closed = []  # A list of hidden cards
for suit in cards.Suit:
    for val in cards.CardValue:
        all_cards_open.append(cards.Card(suit, val))
        all_cards_closed.append(cards.Card(suit, val, False))

print(f"""All cards open __str__ and __int__:\n
{[x for x in map(str, all_cards_open)]}\n
{[x for x in map(int, all_cards_open)]}""")
print(f"""All cards closed __str__ and __int__:\n
{[x for x in map(str, all_cards_closed)]}\n
{[x for x in map(int, all_cards_closed)]}""")
print("\n# ---------------------------------------- Test Hand ---------------------------------------- #\n")
hand = cards.Hand()
print(f"__str__ of Hand with no cards: {hand}")
print(f"value of Hand with no cards: {hand.value}")
hand.cards = [cards.Card(cards.Suit.HEARTS, cards.CardValue.TEN)]
print(f"__str__ of Hand with 1 card: {hand}")
print(f"value of Hand with 1 card: {hand.value}")
hand.cards = [cards.Card(cards.Suit.SPADES, cards.CardValue.ACE), cards.Card(cards.Suit.CLUBS, cards.CardValue.FIVE)]
print(f"__str__ of Hand with 2 cards: {hand}")
print(f"value of Hand with 2 cards: {hand.value}")
hand.cards = [cards.Card(cards.Suit.SPADES, cards.CardValue.ACE),
              cards.Card(cards.Suit.CLUBS, cards.CardValue.TWO),
              cards.Card(cards.Suit.HEARTS, cards.CardValue.EIGHT),
              cards.Card(cards.Suit.DIAMONDS, cards.CardValue.KING)]
print(f"__str__ of Hand with 4 cards: {hand}")
print(f"value of Hand with 4 cards: {hand.value}")
hand.cards = [cards.Card(cards.Suit.SPADES, cards.CardValue.ACE),
              cards.Card(cards.Suit.CLUBS, cards.CardValue.TWO, False),
              cards.Card(cards.Suit.HEARTS, cards.CardValue.EIGHT),
              cards.Card(cards.Suit.DIAMONDS, cards.CardValue.KING)]
print(f"__str__ of Hand with 4 cards, 1 closed: {hand}")
print(f"value of Hand with 4 cards, 1 closed: {hand.value}")
hand.reveal_hand()
print(f"Hand after Hand.reveal_hand: {hand}\nand value: {hand.value}")
print("\n# ---------------------------------------- Test DeckOfCards ---------------------------------------- #\n")
deck_without_jokers = cards.DeckOfCards()
print(f"All cards in deck w/o jokers: {deck_without_jokers.show_cards()}")
deck_without_jokers.shuffle_cards()
print(f"shuffled: {deck_without_jokers.show_cards()}")
print("random card w/o discard:", deck_without_jokers.pick_card(random=True))
print("random card w/ discard:", deck_without_jokers.pick_card(random=True, discard=True))
print("top card w/ discard:", deck_without_jokers.pick_card(discard=True))
print("top card w/ discard and hidden:", deck_without_jokers.pick_card(discard=True, is_open=False))
print("deck length:", len(deck_without_jokers.cards))
print("discarded cards:", deck_without_jokers.discarded_cards)
print("shuffle including discarded cards:", deck_without_jokers.shuffle_cards(True))
print("deck length post shuffle:", len(deck_without_jokers.cards))
print("discarded cards post shuffle:", deck_without_jokers.discarded_cards)

deck_with_jokers = cards.DeckOfCards(True)
print(f"\nAll cards in deck w/ jokers: {deck_with_jokers.show_cards()}")
deck_with_jokers.shuffle_cards()
print(f"shuffled: {deck_with_jokers.show_cards()}")
print("random card w/o discard:", deck_with_jokers.pick_card(random=True))
print("random card w/ discard:", deck_with_jokers.pick_card(random=True, discard=True))
print("top card w/ discard:", deck_with_jokers.pick_card(discard=True))
print("top card w/ discard and hidden:", deck_with_jokers.pick_card(discard=True, is_open=False))
print("deck length:", len(deck_with_jokers.cards))
print("discarded cards:", deck_with_jokers.discarded_cards)
print("shuffle including discarded cards:", deck_with_jokers.shuffle_cards(True))
print("deck length post shuffle:", len(deck_with_jokers.cards))
print("discarded cards post shuffle:", deck_with_jokers.discarded_cards)
