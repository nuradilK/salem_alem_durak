from abc import abstractmethod
from durak.card import Card

class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.hand: list[Card] = []

    @abstractmethod
    def selectAttackingCard(self, table: list[Card]) -> Card:
        pass

    @abstractmethod
    def selectDefendingCard(self) -> Card:
        pass

    def __repr__(self) -> str:
        return self.name

    def willDefendFrom(self, card: Card) -> Card:
        for candidate in self.hand:
            if candidate > card and candidate.sameSuit(card):
                return True
        return False

    def willAttack(self, table: list[Card]) -> bool:
        return self.canAttack(table)

    def canAttack(self, table: list[Card]) -> bool:
        for card in self.hand:
            if self.canAttackWith(table, card):
                return True
        return False

    def canAttackWith(self, table: list[Card], card: Card) -> bool:
        if len(table) == 0:
            return True
        for tableCard in table:
            if card.sameRank(tableCard):
                return True
        return False

    def defend(self, card: Card) -> Card:
        Card = self.selectDefendingCard(card)
        self.removeCard(Card)
        return Card

    def attack(self, table: list[Card]) -> Card:
        card = self.selectAttackingCard(table)
        self.removeCard(card)
        return card

    def takeCard(self, card: Card) -> None:
        self.hand.append(card)

    def printCards(self) -> None:
        print(self.name + "'s cards")
        for card in self.hand:
            print(card, end=', ')
        print()
        
    def removeCard(self, card: Card) -> None:
        indx = self.hand.index(card)
        self.hand.pop(indx)
        self.printCards()

    def shouldTakeCard(self) -> int:
        return len(self.hand) < 6

    def hasCards(self) -> bool:
        return len(self.hand) > 0
    
    def hasWon(self) -> bool:
        return not self.hasCards()
