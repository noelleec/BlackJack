import random
from card import Card

# ==========================================================================
# Deck class

class Deck():
    def __init__(self):
        self.createNewDeck()
        self.shuffle()

    def createNewDeck(self):
        self.__deck = []
        for rank in range(1, 14):
            for suit in range(1, 5):
                self.__deck.append(Card(rank, suit))
    
    def shuffle(self):
        random.shuffle(self.__deck)

    def reset(self):
        self.__init__()

    def deal(self):
        return self.__deck.pop()