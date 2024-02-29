from durak.card import Card
from durak.player import Player

class Bot(Player):
    def __init__(self, name: str) -> None:
        Player.__init__(self, name)

    def selectDefendingCard(self, card: Card) -> Card:
        candidates: list[Card] = []
        for candidate in self.hand:
            if candidate > card and (candidate.sameSuit(card) or candidate.isTrump()):
                candidates.append(candidate)
        sorted_candidates = sorted(candidates)
        print(self, "Defending with", sorted_candidates[0])
        return sorted_candidates[0]

    def selectAttackingCard(self, table: list[Card]) -> Card:
        if len(table) == 0:
            return self.hand[0]
        for card in self.hand:
            for table_card in table:
                if card.sameRank(table_card):
                    return card
