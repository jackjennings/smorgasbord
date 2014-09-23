from unicodeset import UnicodeSet
from .reporter import Reporter


class Smorgasbord(UnicodeSet):

    paths = []

    def __init__(self, iterable):
        super(Smorgasbord, self).__init__(iterable)
        self.reports = Reporter(self, self.__class__.paths)
