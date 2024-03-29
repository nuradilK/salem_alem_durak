from durak.game import Game
from durak.bot import Bot
from durak.human import Human


def main() -> None:
    game = Game()
    aisultan = Bot("Aisultan")
    daulet = Bot("Daulet")
    almas = Human("Almas")

    game.addPlayer(aisultan)
    game.addPlayer(almas)
    game.addPlayer(daulet)

    game.start()


if __name__ == "__main__":
    main()
