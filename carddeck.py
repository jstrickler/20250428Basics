import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self.cards = []  # empty list
        for suit in self.SUITS:
            for rank in self.RANKS:
                new_card = Card(rank, suit)
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    d1.shuffle()
    print(f"{d1.cards = }\n")
    for _ in range(5):
        card = d1.draw()
        print(f"{card = }")
