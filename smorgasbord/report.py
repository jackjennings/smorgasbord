from __future__ import division
import os
from .language import Language
from .coverage import Coverage
from .unicode_set import UnicodeSet

class Report(object):

    def __init__(self, characters, language_file):
        self.characters = self._maybe_make_set(characters)
        self.language = Language.parse(language_file)

    @property
    def coverage(self):
        return Coverage(len(self.covered) / len(self.language.characters))

    @property
    def code(self):
        return self.language.code

    @property
    def covered(self):
        return self.language.characters & self.characters

    @property
    def uncovered(self):
        return self.language.characters - self.characters

    def _maybe_make_set(self, iterable):
        if not isinstance(iterable, set):
            iterable = UnicodeSet(iterable)
        return iterable
