#!/bin/bash/python3
from cards import Cards
import random
class Deck:
    
        def __init__ (self):
            self.cards = []
            self.build()
            self.shuffle()
            self.showcards()
            
        def build (self):
            for s in ['spade','heart','club','diamond']:
                for v in ['ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king']:
                    self.cards.append (Cards(s,v))
                    #print (Cards(s,v).show_card)
                
        def showcards (self):
            for c in self.cards: 
                c.show_card()
                
        def shuffle(self):
            random.shuffle (self.cards)
