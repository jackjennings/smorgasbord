from .unicode_set import UnicodeSet

class Smorgasbord(UnicodeSet):

    language_paths = []

    def __init__(self, *args, **kwargs):
        super(Smorgasbord, self).__init__(*args, **kwargs)
        self.reports = {}
