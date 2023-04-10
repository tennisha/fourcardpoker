from cards import Cards
from Deck import Deck

class Game:
    def __init__(self,deck, numhands):
        self.numhands = numhands
        self.deck = deck
        self.hands = []
    
    def gethand (self, deck,hands):
        self.deck = deck
        self.hands.append (self.deck.cards.pop())
    
    def deal (self,numhands):
        for i in range(numberhands):
            print (deck)
