
class Card:
    # 'self' means 'this instance'
    def __init__(self, rank, suit): # accept arguments 
        self.rank = rank
        self.suit = suit
#        self.wombat = rank

    def __str__(self): # str()
        return f"{self.rank}-{self.suit}"

    def __repr__(self): # repr()
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card('8', 'Diamonds')  # obj = Class(...)
    print(f"{type(c1) = }")
    c2 = Card('5', 'Spades')
    print(f"{c2.rank = }")
    print(f"{c2.suit = }")
    print(f"{c2 = }")
    print(c2)  # str(c2)  HUMAN-friendly
    print(repr(c2))  #  repr()  CODE-friendly "how to reproduce"
