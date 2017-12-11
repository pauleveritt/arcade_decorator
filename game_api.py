from inspect import signature

import arcade


class arcadeapi(arcade.Window):
    _window = None  # This will hold instance of self as "global"
    _game = None  # Class-based games register a game, we store instance

    registry = dict(
        setup=[],
        update=[],
        key_press=[],
        draw=[],
        game=None,
        deferred_drawing=[]
    )

    def __init__(self, width: int, height: int, background_color=None):
        super().__init__(width, height)

        self.width = width
        self.height = height
        if background_color:
            arcade.set_background_color(background_color)

    @classmethod
    def setup(cls):
        for func in cls.registry['setup']:
            if cls._game is not None:
                # Pass game instance as self
                func(cls._game)
            else:
                sig = signature(func)
                if 'window' in sig.parameters:
                    func(cls._window)
                else:
                    func()

    @classmethod
    def on_draw(cls):
        arcade.start_render()

        # Process any deferred imperative drawing
        for drawing in cls.registry['deferred_drawing']:
            this_cmd = getattr(arcade, drawing['cmd'])
            this_args = drawing['args']
            this_kwargs = drawing['kwargs']
            this_cmd(*this_args, **this_kwargs)

        # Now run registered handlers
        for func in cls.registry['draw']:
            if cls._game is not None:
                # Pass game instance as self
                func(cls._game)
            else:
                sig = signature(func)
                if 'window' in sig.parameters:
                    func(cls._window)
                else:
                    func()

    @classmethod
    def update(cls, delta_time):
        for func in cls.registry['update']:
            if cls._game is not None:
                # Pass game instance as self
                func(cls._game, delta_time)
            else:
                sig = signature(func)
                if 'window' in sig.parameters:
                    func(cls._window, delta_time)
                else:
                    func(delta_time)

    @classmethod
    def on_key_press(cls, key, key_modifiers):
        for func in cls.registry['key_press']:
            if cls._game is not None:
                # Pass game instance as self
                func(cls._game, key, key_modifiers)
            else:
                sig = signature(func)
                if 'window' in sig.parameters:
                    func(cls._window, key, key_modifiers)
                else:
                    func(key, key_modifiers)

    # The decorators
    @classmethod
    def init(cls, original_function):
        cls.registry['setup'].append(original_function)
        return original_function

    @classmethod
    def draw(cls, original_function):
        cls.registry['draw'].append(original_function)
        return original_function

    @classmethod
    def animate(cls, original_function):
        cls.registry['update'].append(original_function)
        return original_function

    @classmethod
    def key_press(cls, original_function):
        cls.registry['key_press'].append(original_function)
        return original_function

    @classmethod
    def game(cls, original_game):
        cls.registry['game'] = original_game

    # Now re-implement the arcade drawing methods, to avoid use of
    # global window (for now, faking the re-implementation)
    color = arcade.color
    key = arcade.key

    @classmethod
    def draw_text(cls, *args, **kwargs):
        # Imperative mode means no event-handler functions, simplest
        # possible mode. Detect this by seeing if run has been called. If
        # not, then defer this drawing.
        if cls._window is None:
            cls.registry['deferred_drawing'].append(
                dict(cmd='draw_text', args=args, kwargs=kwargs)
            )
        else:
            arcade.draw_text(*args, **kwargs)

    @classmethod
    def draw_circle_filled(cls, *args, **kwargs):
        if cls._window is None:
            cls.registry['deferred_drawing'].append(
                dict(cmd='draw_circle_filled', args=args, kwargs=kwargs)
            )
        else:
            arcade.draw_circle_filled(*args, **kwargs)

    @classmethod
    def run(cls, width: int = 600, height: int = 400,
            background_color=arcade.color.WHEAT):
        cls._window = arcadeapi(width, height, background_color)
        # If a game is registered, instantiate it
        if cls.registry['game']:
            cls._game = cls.registry['game'](cls._window)
        cls.setup()
        arcade.run()
