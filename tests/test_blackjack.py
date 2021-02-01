from casino.games.blackjack import Blackjack, BlackjackPlayer
from casino.games.cards import DeckOfCards

user = BlackjackPlayer('test')
game = Blackjack(user, DeckOfCards())
game.play()
