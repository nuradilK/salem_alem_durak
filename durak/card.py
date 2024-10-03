from enum import Enum

class Suit(Enum):
    """Enumeration for card suits."""
    SPADES = "♠"
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"

    def __str__(self) -> str:
        return self.value

class Rank(Enum):
    """Enumeration for card ranks."""
    ACE = "A"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"

    def __str__(self) -> str:
        return self.value

class Card:
    """Class representing a playing card."""
    RANK_WEIGHT = {
        Rank.ACE: 14,
        Rank.SIX: 6,
        Rank.SEVEN: 7,
        Rank.EIGHT: 8,
        Rank.NINE: 9,
        Rank.TEN: 10,
        Rank.JACK: 11,
        Rank.QUEEN: 12,
        Rank.KING: 13,
    }

    def __init__(self, suit: Suit, rank: Rank, is_trump: bool) -> None:
        """Initialize a card with a suit, rank, and trump status."""
        self.suit = suit
        self.rank = rank
        self.is_trump = is_trump

    def __repr__(self) -> str:
        """Return a string representation of the card."""
        return f"{self.rank}{self.suit}"

    def weight(self) -> int:
            """Calculate the weight of the card based on its rank and trump status.

            Returns:
                int: The weight of the card.

            Explanation:
                The weight of the card is determined by its rank and trump status. The weight is calculated
                by adding the rank weight to 14 if the card is a trump card. The rank weight is obtained from
                the `RANK_WEIGHT` dictionary.

            """
            weight = self.RANK_WEIGHT[self.rank]
            if self.is_trump:
                weight += 14
            return weight

    def __lt__(self, other: "Card") -> bool:
        """Compare the weight of this card to another."""
        return self.weight() < other.weight()

    def __eq__(self, other: "Card") -> bool:
        """Check if this card is equal to another card."""
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit and self.is_trump == other.is_trump
        return False

    def sameRank(self, card: "Card") -> bool:
        """Check if this card has the same rank as another."""
        return self.rank == card.rank

    def sameSuit(self, card: "Card") -> bool:
        """Check if this card has the same suit as another."""
        return self.suit == card.suit

    def isTrump(self) -> bool:
        """Check if this card is a trump card."""
        return self.is_trump