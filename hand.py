from design import *

# ==========================================================================
# Hand class

ranks = {1: "A", 2: "2", 3: "3", 4:"4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K"}
suits = {1: "♦", 2: "♣", 3: "♥", 4: "♠"}

class Hand():
    def __init__(self, card1, card2):  
        self.__cards = [card1, card2]
        self.__totals = [card1.getValue() + card2.getValue()]
        if card1.isAce() or card2.isAce():
            self.__totals.append(card1.getValue() + card2.getValue() + 10)

    def getTotal(self):
        return self.__totals

    def hit(self, card):
        self.__cards.append(card)
        if (card.isAce()):
            for i in range(len(self.__totals)):
                self.__totals[i] = self.__totals[i] + card.getValue()
                self.__totals.append(self.__totals[i] + 10)
        else:
            for i in range(len(self.__totals)):
                self.__totals[i] = self.__totals[i] + card.getValue()
        
        self.__totals = list(dict.fromkeys(self.__totals))

    def reset(self):
        self.__cards.clear()
        self.__totals.clear()

    def printCards(self, widget):
        totals = self.getTotal()
        if len(totals) > 1 and totals[1] > 21:
            totals.remove(totals[1])
        cardDisplay = str(totals) + " | "
        for card in self.__cards:
            cardDisplay = cardDisplay + ranks[card.getRank()] + " " + suits[card.getSuit()] + " | "
        widget.set(value = cardDisplay)

    def printDealerHand(self):
        cardDisplay = "[?] | " + ranks[self.__cards[0].getRank()] + " " + suits[self.__cards[0].getSuit()] + " | ? |"
        dealersum.set(value = cardDisplay)


