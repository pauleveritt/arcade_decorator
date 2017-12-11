import arcade

from game_api import game


class Ball:
    def __init__(self, radius=20, velocity=70, initial_x=20):
        self.x_position = initial_x
        self.velocity = velocity
        self.radius = radius


@game.init
def setup_my_game(window):
    window.ball: Ball = Ball()


@game.animate
def move_ball(window, delta_time):
    window.ball.x_position += window.ball.velocity * delta_time

    # Did the ball hit the right side of the screen while moving right?
    if window.ball.x_position > window.width - window.ball.radius \
            and window.ball.velocity > 0:
        window.ball.velocity *= -1

    # Did the ball hit the left side of the screen while moving left?
    if window.ball.x_position < window.ball.radius \
            and window.ball.velocity < 0:
        window.ball.velocity *= -1


@game.draw
def draw_the_ball(window):
    arcade.draw_circle_filled(window.ball.x_position, window.height // 2,
                              window.ball.radius, arcade.color.GREEN)


@game.draw
def draw_some_text(window):
    arcade.draw_text("This is a simple template to start your game.",
                     10, window.height // 2, arcade.color.BLACK, 20)


@game.key_press
def press_space(window, key, key_modifiers):
    if key == arcade.key.SPACE:
        print("You pressed the space bar.")


if __name__ == "__main__":
    game.run(700, 600, background_color=arcade.color.MAHOGANY)
