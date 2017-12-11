"""

Simplest possible game, as function.

"""
from game_api import arcadeapi as arcade


@arcade.draw
def draw_hello():
    arcade.draw_text('Hello World', 10, 200, (0, 0, 0), 20)


# Multiple handlers are possible
@arcade.draw
def draw_hello(window):  # window is optional parameter
    msg = f'Optional window argument has width {window.width}'
    arcade.draw_text(msg, 50, 100, (0, 0, 0), 10)


if __name__ == '__main__':
    arcade.run()
