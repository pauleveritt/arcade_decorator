"""

Simplest possible game.

"""
from game_api import arcadeapi as arcade

arcade.draw_text('Hello World', 10, 200, (0, 0, 0), 20)
arcade.run(420, 240, background_color=(100, 100, 100))
