#!/bin/bash/python3
class Cards:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        
    
    def check_suit(self,suit):
        suit_types = ['spade','heart','club','diamond']
        print (self.suit)
        if (self.suit.lower() in suit_types):
          return True
        else:
            return False
          
 
    def check_value (self,value):
            value_types = ['ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king']
            print (self.value)
            if (self.value.lower() in value_types):
                return True
            else: 
                print ('You have entered an incorrect value, Please spell out the card Value. For example a 2 is Two.')
                return False
                
                
