from durak.card import Card
from durak.player import Player

class Human(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def selectCard(self) -> Card:
        while True:
            selected = int(input("Select card to move --> "))
            if not isinstance(selected, int):
                print("The input should be an int")
            elif selected >= len(self.hand):
                print("The provided index is not in range of holding cards")
            else:
                return self.hand[selected]

    def selectAttackingCard(self, table: list[Card]) -> Card:
        print("---------- YOUR CARDS: ----------")
        self.printCards()
        while True:
            card = self.selectCard()
            if self.canAttackWith(table, card):
                break
            else:
                print("You cannot use this card for the attack")
        return card

    def willDefendFrom(self, card: Card):
        if not super().willDefendFrom(card):
            print("You cannot defend the card")
            return False
        print("---------- YOUR CARDS: ----------")
        self.printCards()
        print("Will you defend? (Y/N) ")
        while True:
            result = input().lower()
            if result not in ['y', 'n']:
                print("The input should either Y or N")
            else:
                break
        if result == "y":
            return True
        else:
            return False

    def willAttack(self, table: list[Card]) -> bool:
        if not self.canAttack(table):
            print("You cannot attack")
            return False
        if len(table) == 0:
            return True
        print("---------- YOUR CARDS: ----------")
        self.printCards()
        print("Will you attack? (Y/N) ")
        while True:
            result = input().lower()
            if result not in ['y', 'n']:
                print("The input should either Y or N")
            else:
                break
        if result == "y":
            return True
        else:
            return False

    def selectDefendingCard(self, card: Card) -> Card:
        while True:
            picked_card = self.selectCard()
            if picked_card < card:
                print("The chosen card isn't higher than the attacking card")
            else:
                break
        print("Defending with", picked_card)
        return picked_card
