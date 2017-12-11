import arcade

from game_api import game


@game.key_press
def on_key_press(key):
    if key == arcade.key.SPACE:
        print("You pressed the space bar.")


if __name__ == "__main__":
    game.run()
