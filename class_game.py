"""

Simplest possible game, as a class

"""
import arcade

from game_api import game


class MyGame:
    def __init__(self, starting_text='Hello World'):
        self.starting_text = starting_text

    @game.draw
    def draw_hello(self, window):
        arcade.draw_text(self.starting_text, 10, 100, arcade.color.BLACK, 20)


if __name__ == '__main__':
    game.run()
