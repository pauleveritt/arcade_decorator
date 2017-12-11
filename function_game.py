from arcade import key, color, draw_circle_filled, draw_text

from game_api import game

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_RADIUS = 20


@game.key_press
def press_space(window, key, key_modifiers):
    if key == key.SPACE:
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
    draw_circle_filled(window.ball_x_position, SCREEN_HEIGHT // 2,
                       BALL_RADIUS, color.GREEN)


@game.draw
def draw_some_second_stuff(window):
    draw_text("This is a simple template to start your game.",
              10, SCREEN_HEIGHT // 2, color.BLACK, 20)


if __name__ == "__main__":
    game.run(SCREEN_WIDTH, SCREEN_HEIGHT)
