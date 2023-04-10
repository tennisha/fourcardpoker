#!/bin/bash/python3
class Cards:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        
    
    def check_suit(self,suit):
        suit_types = ['Spade','Heart','Club','Diamond']
        print (self.suit)
        if (self.suit in suit_types):
          return True
        else:
            return False
          
