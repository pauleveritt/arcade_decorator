"""

Class version of function_game

"""
import arcade

from game_api import game


class Ball:
    def __init__(self, radius=20, velocity=70, initial_x=20):
        self.x_position = initial_x
        self.velocity = velocity
        self.radius = radius


@game.world
class MyGame:
    def __init__(self, starting_text='Hello World'):
        self.starting_text = starting_text

        # Don't have to store this on the window this time
        self.ball: Ball = Ball()

    @game.init
    def setup_my_game(self, window):
        # Might still have some work to do on the window after it is
        # constructed
        pass

    @game.animate
    def move_ball(self, window, delta_time):
        self.ball.x_position += self.ball.velocity * delta_time

        # Did the ball hit the right side of the screen while moving right?
        if self.ball.x_position > window.width - self.ball.radius \
                and self.ball.velocity > 0:
            self.ball.velocity *= -1

        # Did the ball hit the left side of the screen while moving left?
        if self.ball.x_position < self.ball.radius \
                and self.ball.velocity < 0:
            self.ball.velocity *= -1

    @game.draw
    def draw_the_ball(self, window):
        arcade.draw_circle_filled(self.ball.x_position, window.height // 2,
                                  self.ball.radius, arcade.color.GREEN)

    @game.draw
    def draw_some_text(self, window):
        arcade.draw_text("This is a simple template to start your game.",
                         10, window.height // 2, arcade.color.BLACK, 20)

    @game.key_press
    def press_space(self, window, key, key_modifiers):
        if key == arcade.key.SPACE:
            print("You pressed the space bar.")


if __name__ == '__main__':
    game.run()
