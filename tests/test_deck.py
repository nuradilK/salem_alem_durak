
import unittest
from durak.card import Card, Suit, Rank
from durak.deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 36)  # 36 cards in a deck

    def test_deck_is_empty(self):
        for _ in range(36):  # Draw all cards
            self.deck.drawCard()
        self.assertTrue(self.deck.isEmpty())

    def test_deck_draw_card(self):
        card = self.deck.drawCard()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(self.deck.cards), 35)  # One card has been drawn

    def test_deck_draw_card_empty(self):
        for _ in range(36):  # Draw all cards
            self.deck.drawCard()
        card = self.deck.drawCard()  # Try to draw from an empty deck
        self.assertIsNone(card)

    def test_deck_contents(self):
        expected_cards = []
        for suit in Suit:
            for rank in Rank:
                expected_cards.append(Card(suit, rank, self.deck.getTrumpSuit() == suit))

        self.assertCountEqual(self.deck.cards, expected_cards)
    

if __name__ == "__main__":
    unittest.main()

