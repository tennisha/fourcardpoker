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
        print ("number of hands is " +str(self.numhands) )
        i=0
        while (i<self.numhands):
            print (str(i) + " is the value of i and start is "+str(start))
            
            nexthand = deck.shownumcards(start,start+5)
            print (nexthand)
            allhands = allhands+nexthand
            i+=1
            start+=5
        #print(deck.showcards)
        #print ('Your hand is '+ self.hands[0]) 
    
    def deal (self,numhands):
        for i in range(numberhands):
            print (deck)
