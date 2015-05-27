
import inspect

from functools import wraps


def fluent(method):
    @wraps(method)
    def inner(*args, **kwargs):
        method(*args, **kwargs)

        return method.im_self

    return inner


class Bype(object):
    def __new__(cls, *args, **kwargs):
        self = object.__new__(cls, *args, **kwargs)

        for name in dir(self):
            attr = getattr(self, name)

            if inspect.ismethod(attr) and not name.startswith('_'):
                print attr
                setattr(self, name, fluent(attr))

        return self
