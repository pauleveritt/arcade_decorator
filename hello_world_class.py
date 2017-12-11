"""

Simplest possible game, as class.

"""

from game_api import arcadeapi as arcade


@arcade.game
class HelloWorld:
    def __init__(self, window: arcade):
        self.window = window

    @arcade.draw
    def draw_hello(self):
        arcade.draw_text('Hello World', 10, 100, (0, 0, 0), 20)


if __name__ == '__main__':
    arcade.run()
