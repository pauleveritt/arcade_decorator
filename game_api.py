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
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last
        # frame.
        arcade.start_render()

        # Draw the circle
        arcade.draw_circle_filled(self.ball_x_position, SCREEN_HEIGHT // 2,
                                  BALL_RADIUS, arcade.color.GREEN)

        # Draw the text
        arcade.draw_text("This is a simple template to start your game.",
                         10, SCREEN_HEIGHT // 2, arcade.color.BLACK, 20)

    def update(self, delta_time):
        # Move the ball
        self.ball_x_position += self.ball_x_pixels_per_second * delta_time

        # Did the ball hit the right side of the screen while moving right?
        if self.ball_x_position > SCREEN_WIDTH - BALL_RADIUS \
                and self.ball_x_pixels_per_second > 0:
            self.ball_x_pixels_per_second *= -1

        # Did the ball hit the left side of the screen while moving left?
        if self.ball_x_position < BALL_RADIUS \
                and self.ball_x_pixels_per_second < 0:
            self.ball_x_pixels_per_second *= -1

    def on_key_press(self, key, key_modifiers):
        for func in self.base_game.registry:
            func(key)


@singleton_object
class game(metaclass=Singleton):
    registry = []

    def __init__(self):
        self.window = GameWindow(self, SCREEN_WIDTH, SCREEN_HEIGHT)

    @classmethod
    def key_press(cls, original_function):
        cls.registry.append(original_function)
        return original_function

    @classmethod
    def run(cls, *args, **kwargs):
        arcade.run()
