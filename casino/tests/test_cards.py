from casino.games import cards

deck = cards.DeckOfCards(jokers=True)
deck.shuffle_cards()
print("random card w/o discard:", deck.pick_random_card())
print("random card w/ discard:", deck.pick_top_card(True))
print("random card w/ discard:", deck.pick_top_card(True))
print("deck length:", len(deck.cards))
print("discarded cards:", deck.discarded_cards)
print("shuffle including discarded cards:", deck.shuffle_cards(True))
print("deck length post shuffle:", len(deck.cards))
print("discarded cards post shuffle:", deck.discarded_cards)