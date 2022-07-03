# ==========================================================================
# Card class

class Card():
    def __init__(self, rank, suit):
        self.__rank = rank     
        self.__suit = suit

    def getRank(self):
        return self.__rank

    def getValue(self):
        if self.__rank in range(11, 14):
            return 10
        return self.__rank

    def getSuit(self):
        return self.__suit

    def isAce(self):
        return self.__rank == 1