from test.test_datetime import suit
from random import shuffle
class Card:
    
    def __init(self,value,suit):
        self.suit = suit
        self.value = value
        
        
    def __repre__(self):
        return f"{self.value} of {self.suit}"
    

class Desk:
       
    def __init__(self):
        suits = ["Hearts","Diamond","Clubs","Spades"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] 
        self.cards = [] #[Card(value,suit) for suit in suits for value in values]
        for suit in suits:
            for value in values:
                self.cards.append(Card(value,suit))
    
    def __repre__(self): 
        return  "f Desk of {self.card()} cards"   
    
    def count(self):
        return len(self.cards)
        
    def _deal(self,number):   
        count = self.count()
        actual = min([number,count])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
        
    def shuffle(self):
        if self.count<52:
            raise ValueError("only full desk can be suffled")
        shuffle(self.cards)
        
    
    
    def deal_crad(self):
        return self._deal(1)[0]
    
    def deal_hand(self,n):
        return self._deal(n)
    
        
mydesk = Desk()
print(mydesk)
mydesk.suffle()
card=mydesk.deal_card()
print(card)
hand = mydesk.deal_hand(5)
print(mydesk)
        
        