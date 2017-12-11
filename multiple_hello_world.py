"""

Simplest possible game, as function.

"""
from game_api import game


@game.draw
def draw_hello():
    game.draw_text('Hello World', 10, 200, (0, 0, 0), 20)


# Multiple handlers are possible
@game.draw
def draw_hello(window):  # window is optional parameter
    msg = f'Optional window argument has width {window.width}'
    game.draw_text(msg, 50, 100, (0, 0, 0), 10)


if __name__ == '__main__':
    game.run()
