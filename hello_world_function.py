"""

Simplest possible game, as function.

"""
from game_api import arcadeapi as arcade


@arcade.draw
def draw_hello():
    arcade.draw_text('Hello World', 10, 200, (0, 0, 0), 20)


if __name__ == '__main__':
    arcade.run(420, 240, title='Hi', background_color=(100, 100, 100))
