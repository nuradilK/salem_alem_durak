import random
from durak.card import Card, Suit, Rank


class Deck:
    def __init__(self):
        self.cards: list[Card] = []
        self.trump_suit = random.choice(list(Suit))
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(suit, rank, self.trump_suit == suit))
        random.shuffle(self.cards)
        print(f"\t\tTrump suit is {self.trump_suit}")
        print(self.cards)

    def isEmpty(self) -> bool:
        return len(self.cards) == 0

    def getTrumpSuit(self) -> Suit:
        return self.trump_suit

    def drawCard(self) -> Card:
        if len(self.cards) > 0:
            drawnCard = self.cards.pop(0)
            print("\t\tDrawn from deck", drawnCard)
            return drawnCard
        return None
