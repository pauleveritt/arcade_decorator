"""

Simplest possible game, as class.

"""

from game_api import game


@game.world
class HelloWorld:
    def __init__(self, window: game):
        self.window = window

    @game.draw
    def draw_hello(self):
        game.draw_text('Hello World', 10, 100, (0, 0, 0), 20)


if __name__ == '__main__':
    game.run()
