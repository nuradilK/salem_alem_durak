from enum import Enum

class Suit(Enum):
    SPADES = '♠'
    HEARTS = '♥'
    DIAMONDS = '♦'
    CLUBS = '♣'

    def __str__(self) -> str:
        return self.value

class Rank(Enum):
    ACE = 'A'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'

    def __str__(self) -> str:
        return self.value

class Card:
    RANK_WEIGHT = {
        Rank.ACE: 14,
        Rank.TWO: 2,
        Rank.THREE: 3,
        Rank.FOUR: 4,
        Rank.FIVE: 5,
        Rank.SIX: 6,
        Rank.SEVEN: 7,
        Rank.EIGHT: 8,
        Rank.NINE: 9,
        Rank.TEN: 10,
        Rank.JACK: 11,
        Rank.QUEEN: 12,
        Rank.KING: 13,
    }

    def weight(self) -> int:
        return Rank.WEIGHT[self.name]

    def __init__(self, suit: Suit, rank: Rank, is_trump: bool) -> None:
        self.suit = suit
        self.rank = rank
        self.is_trump = is_trump
    def __repr__(self) -> str:
        return f'{self.rank}{self.suit}'

    def weight(self) -> int:
        weight = self.RANK_WEIGHT[self.rank]
        if self.is_trump:
            weight += 14
        return weight

    def __lt__(self, other: 'Card') -> bool:
        return self.weight() < other.weight()

    def sameRank(self, card: 'Card') -> bool:
        return self.rank == card.rank

    def sameSuit(self, card: 'Card') -> bool:
        return self.suit == card.suit
        
    def isTrump(self) -> bool:
        return self.is_trump
