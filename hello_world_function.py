"""

Simplest possible game, as function.

"""
from game_api import game


@game.draw
def draw_hello():
    game.draw_text('Hello World', 10, 200, (0, 0, 0), 20)


if __name__ == '__main__':
    game.run()
