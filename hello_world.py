"""

Simplest possible game.

"""
import arcade

from game_api import game


@game.draw
def draw_hello(window):
    arcade.draw_text('Hello World', 10, 100, arcade.color.BLACK, 20)


if __name__ == '__main__':
    game.run()
