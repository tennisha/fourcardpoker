from cards import Cards
from Deck import Deck

class Game:
    def __init__(self,deck, numhands):
        self.numhands = numhands
        self.deck = deck
        self.hands = []
        self.gethand(self.deck,0,5)
    
    def gethand (self,deck,start,hands):
        allhands = []
        i=0
        while (i<self.numhands):
            allhands.append(deck.shownumcards(start,hands))
            i+=1
            start+=5
        #print(deck.showcards)
        #print ('Your hand is '+ self.hands[0]) 
    
    def deal (self,numhands):
        for i in range(numberhands):
            print (deck)
