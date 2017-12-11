# Experimental decorator-based game API for Arcade

This repo has some games that show an new, parallel, alternative 
API for making games:

* hello_world.py has an imperative approach
* hello_world_function.py is a tiny function-based approach
* hello_world_class.py is the same, class-based
* multiple_hello_world.py shows two handlers, one with an optional 
argument
* function_game.py and class_game.py show a bit more

This API currently shows the following:

* Imperative eliminates construction of window, set background 
color, and start render. You can pass arguments to run to customize 
some window stuff (width, height, title, background color.)

* Eliminates `start_render` by having the decorator construct 
the window and call start_render.

* Multiple handlers can be attached for the same event.

* We can present an alternative to the pyglet API

* Your functions can skip asking for a window, or if they ask, we'll 
sniff at it and supply it.

* Parallel (currently faked) versions of the Arcade API which 
don't use a global window.

## Goals

* Eliminate some annoyances (start_render, imperative has to construct 
a window, window as a global, making a user implement a window when 
they want to implement a game)
* Any global state can be easily reset (restarting a game, 
testing, etc.)  
* Sensible defaults: optional, and choosable

## Questions

* To avoid global window, while preserving previous API, 
probably means some major reshuffling. Perhaps mirror on 
game e.g. game.draw_text
  
* We probably could make this do some batching/layers implicitly, without 
the user thinking about it