"""

Class version of function_game

"""
import arcade

from game_api import arcadeapi as arcade


class Ball:
    def __init__(self, radius=20, velocity=70, initial_x=20):
        self.x_position = initial_x
        self.velocity = velocity
        self.radius = radius


@arcade.game
class MyGame:
    def __init__(self, window: arcade):
        self.window = window
        self.starting_text = 'Hello World'

        # Don't have to store this on the window this time
        self.ball: Ball = Ball()

    @arcade.animate
    def move_ball(self, delta_time):
        self.ball.x_position += self.ball.velocity * delta_time

        # Did the ball hit the right side of the screen while moving right?
        if self.ball.x_position > self.window.width - self.ball.radius \
                and self.ball.velocity > 0:
            self.ball.velocity *= -1

        # Did the ball hit the left side of the screen while moving left?
        if self.ball.x_position < self.ball.radius \
                and self.ball.velocity < 0:
            self.ball.velocity *= -1

    @arcade.draw
    def draw_the_ball(self):
        arcade.draw_circle_filled(self.ball.x_position,
                                  self.window.height // 2,
                                  self.ball.radius, arcade.color.GREEN)

    @arcade.draw
    def draw_some_text(self):
        arcade.draw_text("This is a simple template to start your game.",
                         10, self.window.height // 2, arcade.color.BLACK, 20)

    @arcade.key_press
    def press_space(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            print("You pressed the space bar.")


if __name__ == '__main__':
    arcade.run()
