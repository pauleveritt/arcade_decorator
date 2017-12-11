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
color, and start render.

* Eliminates `start_render` by having the decorator construct 
the window and call start_render.

* Multiple handlers can be attached for the same event.

* We can present an alternative to the pyglet API

* Optional arguments (e.g. window)

* Parallel (currently faked) versions of the Arcade API which 
don't use a global window.

## Goals

* Promote the use/value of type hinting

* Any global state can be easily reset (restarting a game, 
testing, etc.)
  
* Sensible defaults: optional, and choosable

## Implementation Notes

* You can have as many functions as you want for a handler, 
might want a sorting mechanism later

* For class-based programs, what's the purpose of the class? 
It's no longer needed to be the pyglet machinery. Let's say 
it is to have a top-level domain-specific "world".

* For function-based, allow "window" to be optional by 
sniffing the signature to see if they ask for it.

## Questions

* To avoid global window, while preserving previous API, 
probably means some major reshuffling. Perhaps mirror on 
game e.g. game.draw_text
  
