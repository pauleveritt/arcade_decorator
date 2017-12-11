
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

* For function-based, we could allow "window" to be optional 
by sniffing the signature to see if they ask for it.

## Questions

* To avoid global window, while preserving previous API, 
probably means some major reshuffling. Perhaps mirror on 
game e.g. game.draw_text
  
