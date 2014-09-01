from __future__ import print_function

__version__ = "0.0.1"

class Smorgasbord(set):
    
    def __init__(self, iterable):
        iterable = [self._encode(c) for c in iterable]
        super(Smorgasbord, self).__init__(iterable)

    def __contains__(self, char):
        return super(Smorgasbord, self).__contains__(self._encode(char))

    def _encode(self, char):
        if isinstance(char, int):
            try:
                return unichr(char)
            except Exception:
                return chr(char)
        else:
            try:
                return unicode(char)
            except Exception:
                return char
