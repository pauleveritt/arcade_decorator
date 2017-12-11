import datetime
import time


class Window:
    pass


class World:
    def __init__(self, window: Window):
        self.window = window


class timing:
    def __init__(self):
        print('init')

    @classmethod
    def time_this(cls, original_function):
        def new_function(*args, **kwargs):
            before = datetime.datetime.now()
            x = original_function(*args, **kwargs)
            after = datetime.datetime.now()
            print("Elapsed Time = {0}".format(after - before))
            return x

        return new_function

    @classmethod
    def run(cls, *args, **kwargs):
        pass

@timing.time_this
def func_a(stuff):
    time.sleep(1)


if __name__ == '__main__':
    func_a(1)
