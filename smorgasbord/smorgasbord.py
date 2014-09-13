from .unicode_set import UnicodeSet
from .reporter import Reporter

class Smorgasbord(object):

    language_paths = []

    def __init__(self, iterable):
        self.set = UnicodeSet(iterable)
        self.reports = Reporter(self.set, self.__class__.language_paths)

    def __iter__(self):
        return iter(self.set)

    def add(self, value):
        return self.set.add(value)
