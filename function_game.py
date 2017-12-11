import arcade

from game_api import game, SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS


@game.key_press
def press_space(window, key, key_modifiers):
    if key == arcade.key.SPACE:
        print("You pressed the space bar.")


@game.update
def move_ball(window, delta_time):
    window.ball_x_position += window.ball_x_pixels_per_second * delta_time

    # Did the ball hit the right side of the screen while moving right?
    if window.ball_x_position > SCREEN_WIDTH - BALL_RADIUS \
            and window.ball_x_pixels_per_second > 0:
        window.ball_x_pixels_per_second *= -1

    # Did the ball hit the left side of the screen while moving left?
    if window.ball_x_position < BALL_RADIUS \
            and window.ball_x_pixels_per_second < 0:
        window.ball_x_pixels_per_second *= -1


@game.draw
def draw_some_first_stuff(window):
    arcade.draw_circle_filled(window.ball_x_position, SCREEN_HEIGHT // 2,
                              BALL_RADIUS, arcade.color.GREEN)


@game.draw
def draw_some_second_stuff(window):
    arcade.draw_text("This is a simple template to start your game.",
                     10, SCREEN_HEIGHT // 2, arcade.color.BLACK, 20)


if __name__ == "__main__":
    game.run()
