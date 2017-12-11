"""

Simplest possible game, as class.

"""
import arcade

from game_api import game


@game.world
class HelloWorld:
    def __init__(self, window: game):
        self.window = window

    @game.draw
    def draw_hello(self):
        arcade.draw_text('Hello World', 10, 100, arcade.color.BLACK, 20)


if __name__ == '__main__':
    game.run()
