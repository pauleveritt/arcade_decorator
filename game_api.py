"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

A walk-through of this code is available at:
https://vimeo.com/168051968
"""
import arcade

from singleton import singleton_object, Singleton

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
BALL_RADIUS = 20


class GameWindow(arcade.Window):

    def __init__(self, base_game, width, height):
        super().__init__(width, height)

        self.base_game = base_game

        self.ball_x_position = BALL_RADIUS
        self.ball_x_pixels_per_second = 70

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()

        for func in self.base_game.registry['draw']:
            func(self)

    def update(self, delta_time):
        for func in self.base_game.registry['update']:
            func(self, delta_time)

    def on_key_press(self, key, key_modifiers):
        for func in self.base_game.registry['key_press']:
            func(self, key, key_modifiers)


@singleton_object
class game(metaclass=Singleton):
    registry = dict(
        update=[],
        key_press=[],
        draw=[]
    )

    def __init__(self):
        self.window = GameWindow(self, SCREEN_WIDTH, SCREEN_HEIGHT)

    @classmethod
    def draw(cls, original_function):
        cls.registry['draw'].append(original_function)
        return original_function

    @classmethod
    def update(cls, original_function):
        cls.registry['update'].append(original_function)
        return original_function

    @classmethod
    def key_press(cls, original_function):
        cls.registry['key_press'].append(original_function)
        return original_function

    @classmethod
    def run(cls, *args, **kwargs):
        arcade.run()
