"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

A walk-through of this code is available at:
https://vimeo.com/168051968
"""
import arcade

from singleton import singleton_object, Singleton


class GameWindow(arcade.Window):

    def __init__(self, base_game, width: int, height: int):
        super().__init__(width, height)

        self.base_game: game = base_game
        self.width = width
        self.height = height
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        for func in self.base_game.registry['setup']:
            func(self)

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
    window: GameWindow
    registry = dict(
        setup=[],
        update=[],
        key_press=[],
        draw=[]
    )

    def __init__(self):
        self.flag = 99

    @classmethod
    def setup(cls, original_function):
        cls.registry['setup'].append(original_function)
        return original_function

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
    def run(cls, width: int = 600, height: int = 400, **kwargs):
        cls.window = GameWindow(cls, width, height)
        cls.window.setup()
        arcade.run()
