import random

class Card:
    
    def __init__(self, sSuit, sValue, nValue):
        self.sSuit = sSuit
        self.sValue = sValue
        self.nValue = nValue
        
    def getValue(self):
        return self.nValue

    def getStringValue(self):
        return self.sValue

    def getSuit(self):
        return self.sSuit

    def __str__(self):
        stringValue = self.getStringValue()
        stringSuit = self.getSuit()
    
        card = stringValue + " of " + stringSuit + " "
        return card
    
class Deck:
    
    def __init__(self):
        self.sizeOfDeck = 52
        self.cards = []
        
        suitList = ["Spades", "Hearts", "Diamonds", "Clubs"]
        valueList = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                 "Nine", "Ten", "Jack", "Queen", "King"]
        
        for suit in range(4):
            for value in range(13):
                card = Card(suitList[suit], valueList[value], value+1)
                self.cards.append(card)
                
    def shuffleDeck(self):
        random.shuffle(self.cards)
        
    def getCard(self):
        
        cardToDeal = self.cards[-1]
        self.sizeOfDeck -= 1
        self.cards.pop()
        
        return cardToDeal
    
    def size(self):
        return self.sizeOfDeck

deck = Deck()
deck.shuffleDeck()

while deck.size() > 0:
    card = deck.getCard()
    print(str(card))
    

        
        
        
        
                
        
        
