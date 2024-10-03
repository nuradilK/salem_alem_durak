import unittest
from durak.player import Player
from durak.card import Card, Rank, Suit

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("John")

    def test_init(self):
        self.assertEqual(self.player.name, "John")
        self.assertEqual(self.player.hand, [])

    def test_repr(self):
        self.assertEqual(repr(self.player), "John")

    def test_willDefendFrom(self):
        card1 = Card(Suit.HEARTS, Rank.ACE, False)
        card2 = Card(Suit.HEARTS, Rank.KING, False)
        card3 = Card(Suit.SPADES, Rank.KING, False)
        self.player.hand = [card1, card2, card3]
        self.assertTrue(self.player.willDefendFrom(card1))
        self.assertFalse(self.player.willDefendFrom(card2))
        self.assertFalse(self.player.willDefendFrom(card3))

    def test_willAttack(self):
        table = [Card(Suit.HEARTS, Rank.ACE, False)]
        self.player.hand = [Card(Suit.HEARTS, Rank.KING, False)]
        self.assertTrue(self.player.willAttack(table))

    def test_canAttack(self):
        table = [Card(Suit.HEARTS, Rank.ACE, False)]
        self.player.hand = [Card(Suit.HEARTS, Rank.KING, False)]
        self.assertTrue(self.player.canAttack(table))

    def test_canAttackWith(self):
        table = [Card(Suit.HEARTS, Rank.ACE, False)]
        card1 = Card(Suit.HEARTS, Rank.KING, False)
        card2 = Card(Suit.SPADES, Rank.KING, False)
        self.player.hand = [card1, card2]
        self.assertTrue(self.player.canAttackWith(table, card1))
        self.assertFalse(self.player.canAttackWith(table, card2))

    def test_defend(self):
        card = Card(Suit.HEARTS, Rank.ACE, False)
        self.player.hand = [card]
        self.assertEqual(self.player.defend(card), card)
        self.assertEqual(self.player.hand, [])

    def test_attack(self):
        table = [Card(Suit.HEARTS, Rank.ACE, False)]
        card = Card(Suit.HEARTS, Rank.KING, False)
        self.player.hand = [card]
        self.assertEqual(self.player.attack(table), card)
        self.assertEqual(self.player.hand, [])

    def test_takeCard(self):
        card = Card(Suit.HEARTS, Rank.ACE, False)
        self.player.takeCard(card)
        self.assertEqual(self.player.hand, [card])

    def test_removeCard(self):
        card1 = Card(Suit.HEARTS, Rank.ACE, False)
        card2 = Card(Suit.HEARTS, Rank.KING, False)
        self.player.hand = [card1, card2]
        self.player.removeCard(card1)
        self.assertEqual(self.player.hand, [card2])

    def test_shouldTakeCard(self):
        self.player.hand = [Card(Suit.HEARTS, Rank.ACE, False)]
        self.assertTrue(self.player.shouldTakeCard())
        self.player.hand = [Card(Suit.HEARTS, Rank.ACE, False)] * 6
        self.assertFalse(self.player.shouldTakeCard())

    def test_hasCards(self):
        self.assertFalse(self.player.hasCards())
        self.player.hand = [Card(Suit.HEARTS, Rank.ACE, False)]
        self.assertTrue(self.player.hasCards())

    def test_hasWon(self):
        self.assertTrue(self.player.hasWon())
        self.player.hand = [Card(Suit.HEARTS, Rank.ACE, False)]
        self.assertFalse(self.player.hasWon())

if __name__ == "__main__":
    unittest.main()