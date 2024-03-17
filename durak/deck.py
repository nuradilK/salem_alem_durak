import random
from durak.card import Card, Suit, Rank


class Deck:
    def __init__(self):
        self.cards: list[Card] = []
        trump_suit = random.choice(list(Suit))
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(suit, rank, trump_suit == suit))
        random.shuffle(self.cards)
        print(f"\t\tTrump suit is {trump_suit}")
        print(self.cards)

    def isEmpty(self) -> bool:
        return len(self.cards) == 0

    def drawCard(self) -> Card:
        if len(self.cards) > 0:
            drawnCard = self.cards.pop(0)
            print("\t\tDrawn from deck", drawnCard)
            return drawnCard
        return None
