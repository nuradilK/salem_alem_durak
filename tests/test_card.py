import unittest
from durak.card import Card, Rank, Suit

class TestCard(unittest.TestCase):
    def test_init(self):
        card = Card(Suit.HEARTS, Rank.ACE, False)
        self.assertEqual(card.suit, Suit.HEARTS)
        self.assertEqual(card.rank, Rank.ACE)
        self.assertFalse(card.is_trump)

    def test_repr_king_of_diamonds(self):
        card = Card(Suit.DIAMONDS, Rank.KING, True)
        self.assertEqual(repr(card), "K♦")

    def test_repr_ace_of_spades(self):
        card = Card(Suit.SPADES, Rank.ACE, True)
        self.assertEqual(repr(card), "A♠")

    def test_repr_queen_of_hearts(self):
        card = Card(Suit.HEARTS, Rank.QUEEN, True)
        self.assertEqual(repr(card), "Q♥")

    def test_repr_jack_of_clubs(self):
        card = Card(Suit.CLUBS, Rank.JACK, True)
        self.assertEqual(repr(card), "J♣")

    def test_repr_ten_of_diamonds(self):
        card = Card(Suit.DIAMONDS, Rank.TEN, True)
        self.assertEqual(repr(card), "10♦")

    def test_weight(self):
        card1 = Card(Suit.CLUBS, Rank.SIX, False)
        card2 = Card(Suit.SPADES, Rank.JACK, True)
        self.assertEqual(card1.weight(), 6)
        self.assertEqual(card2.weight(), 25)

    def test_weight_ace(self):
        card = Card(Suit.HEARTS, Rank.ACE, False)
        self.assertEqual(card.weight(), 14)

    def test_weight_queen(self):
        card = Card(Suit.DIAMONDS, Rank.QUEEN, True)
        self.assertEqual(card.weight(), 26)

    def test_weight_king(self):
        card = Card(Suit.CLUBS, Rank.KING, True)
        self.assertEqual(card.weight(), 27)

    def test_weight_ten(self):
        card = Card(Suit.SPADES, Rank.TEN, False)
        self.assertEqual(card.weight(), 10)

    def test_lt(self):
        card1 = Card(Suit.HEARTS, Rank.QUEEN, False)
        card2 = Card(Suit.DIAMONDS, Rank.KING, False)
        self.assertLess(card1, card2)

    def test_sameRank(self):
        card1 = Card(Suit.CLUBS, Rank.TEN, False)
        card2 = Card(Suit.SPADES, Rank.TEN, True)
        self.assertTrue(card1.sameRank(card2))

    def test_sameSuit(self):
        card1 = Card(Suit.HEARTS, Rank.JACK, False)
        card2 = Card(Suit.HEARTS, Rank.QUEEN, False)
        self.assertTrue(card1.sameSuit(card2))

    def test_isTrump(self):
        card1 = Card(Suit.CLUBS, Rank.ACE, False)
        card2 = Card(Suit.SPADES, Rank.KING, True)
        self.assertFalse(card1.isTrump())
        self.assertTrue(card2.isTrump())

if __name__ == "__main__":
    unittest.main()