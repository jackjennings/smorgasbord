class UnicodeSet(set):

    def __init__(self, iterable):
        iterable = [self._encode(c) for c in iterable]
        super(UnicodeSet, self).__init__(iterable)

    def __contains__(self, char):
        return super(UnicodeSet, self).__contains__(self._encode(char))

    def __iter__(self):
        return iter(sorted(set(self), key=ord))

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
