"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

A walk-through of this code is available at:
https://vimeo.com/168051968
"""
import arcade


class game(arcade.Window):
    window = None  # This will hold instance of self as "global"

    registry = dict(
        setup=[],
        update=[],
        key_press=[],
        draw=[]
    )

    def __init__(self, width: int, height: int, background_color=None):
        super().__init__(width, height)

        self.width = width
        self.height = height
        if background_color:
            arcade.set_background_color(background_color)

    @classmethod
    def setup(cls):
        for func in cls.registry['setup']:
            func(cls.window)

    @classmethod
    def on_draw(cls):
        arcade.start_render()

        for func in cls.registry['draw']:
            func(cls.window)

    @classmethod
    def update(cls, delta_time):
        for func in cls.registry['update']:
            func(cls.window, delta_time)

    @classmethod
    def on_key_press(cls, key, key_modifiers):
        for func in cls.registry['key_press']:
            func(cls.window, key, key_modifiers)

    # The decorators
    @classmethod
    def init(cls, original_function):
        cls.registry['setup'].append(original_function)
        return original_function

    @classmethod
    def draw(cls, original_function):
        cls.registry['draw'].append(original_function)
        return original_function

    @classmethod
    def animate(cls, original_function):
        cls.registry['update'].append(original_function)
        return original_function

    @classmethod
    def key_press(cls, original_function):
        cls.registry['key_press'].append(original_function)
        return original_function

    @classmethod
    def run(cls, width: int = 600, height: int = 400,
            background_color=arcade.color.WHEAT):
        cls.window = game(width, height, background_color)
        cls.setup()
        arcade.run()

#
# @singleton_object
# class game(metaclass=Singleton):
#     window: GameWindow
#     registry = dict(
#         setup=[],
#         update=[],
#         key_press=[],
#         draw=[]
#     )
#
#     def __init__(self):
#         self.flag = 99  # Not used at all, might want to re-think later
#
#     @classmethod
#     def setup(cls, original_function):
#         cls.registry['setup'].append(original_function)
#         return original_function
#
#     @classmethod
#     def draw(cls, original_function):
#         cls.registry['draw'].append(original_function)
#         return original_function
#
#     @classmethod
#     def update(cls, original_function):
#         cls.registry['update'].append(original_function)
#         return original_function
#
#     @classmethod
#     def key_press(cls, original_function):
#         cls.registry['key_press'].append(original_function)
#         return original_function
#
#     @classmethod
#     def run(cls, width: int = 600, height: int = 400,
#             background_color=arcade.color.WHEAT):
#         cls.window = GameWindow(cls, width, height, background_color)
#         cls.window.setup()
#         arcade.run()
