from .unicode_set import UnicodeSet
from .reporter import Reporter

class Smorgasbord(UnicodeSet):

    language_paths = []

    def __init__(self, *args, **kwargs):
        super(Smorgasbord, self).__init__(*args, **kwargs)
        self.reports = Reporter(self, self.__class__.language_paths)
