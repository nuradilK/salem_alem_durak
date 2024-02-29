from enum import Enum
from typing import Optional

from durak.card import Card
from durak.deck import Deck
from durak.player import Player

class GameOutcome(Enum):
    PHASE_STATUS_DEFENDED = 0
    PHASE_STATUS_SURRENDERED = 1

class Game:
    def __init__(self) -> None:
        self.deck: Deck = Deck()
        self.players: list[Player] = []
        self.activePlayer: Optional[Player] = None
        self.lastCard: Optional[Card] = None
        self.table: list[Card] = []

    def addPlayer(self, player: Player) -> None:
        if len(self.players) == 6:
            raise RuntimeError('There can be at most 6 players')
        self.players.append(player)
        if self.activePlayer == None:
            self.activePlayer = player

    def start(self) -> None:
        print("Dealing cards")
        self.deal()
        self.printCards()
        print("Starting game")
        while not self.finished():
            outcome = self.phase()
            self.clearTable()
            print("~~~~~~~~~ PHASE COMPLETED ~~~~~~~~~")
            self.fillHands()
            self.moveTurn(outcome)
        print("Player", self.activePlayer, "lost")

    def moveTurn(self, outcome: GameOutcome) -> None:
        if outcome == GameOutcome.PHASE_STATUS_DEFENDED:
            self.activePlayer = self.nextPlayer()
        else:
            self.activePlayer = self.nextPlayer()
            self.activePlayer = self.nextPlayer()

    def deal(self) -> None:
        for player in self.players:
            for _ in range(6):
                player.takeCard(self.deck.drawCard())

    def printCards(self) -> None:
        for player in self.players:
            player.printCards()

    def phase(self) -> None:
        attacker = self.attackingPlayer()
        defender = self.defendingPlayer()
        while True:
            if not attacker.willAttack(self.table):
                return GameOutcome.PHASE_STATUS_DEFENDED
            self.lastCard = self.attack()
            if not defender.willDefendFrom(self.lastCard):
                print(defender, "Can't defend from", self.lastCard)
                return GameOutcome.PHASE_STATUS_SURRENDERED
            self.lastCard = self.defend()

    def attack(self) -> Card:
        attackingPlayer = self.attackingPlayer()
        print("Table", self.table)
        attackingCard = attackingPlayer.attack(self.table)
        self.addCardToTable(attackingCard)
        print(attackingPlayer, "Attacking with", attackingCard)
        return attackingCard

    def defend(self) -> Card: 
        defendingCard = self.defendingPlayer().defend(self.lastCard)
        self.addCardToTable(defendingCard)
        return defendingCard

    def fillHands(self) -> None:
        for player in self.players:
            while player.shouldTakeCard():
                drawnCard = self.deck.drawCard()
                if drawnCard is not None:
                    player.takeCard(drawnCard)
                else:
                    break

    def clearTable(self) -> None:
        for card in self.table:
            self.defendingPlayer().takeCard(card)
        self.table = []

    def nextPlayer(self) -> Player:
        idx = self.players.index(self.activePlayer)
        next_idx = idx + 1
        if next_idx == len(self.players):
            next_idx = 0
        return self.players[next_idx]

    def defendingPlayer(self) -> Player:
        return self.nextPlayer()

    def attackingPlayer(self) -> Player:
        return self.activePlayer

    def addCardToTable(self, card: Card) -> None:
        self.table.append(card)

    def deckIsEmpty(self) -> bool:
        return self.deck.isEmpty()

    def finished(self) -> bool:
        if not self.deckIsEmpty():
            return False
        num_player_with_cards = 0
        for player in self.players:
            if player.hasCards():
                num_player_with_cards += 1
        return num_player_with_cards == 1
