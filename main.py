"""
Platformer Game
"""
import game


def main():
    """ Main method """
    window = game.MyGame()
    window.setup()
    game.arcade.run()


if __name__ == "__main__":
    main()
