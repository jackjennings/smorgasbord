from __future__ import division
import os
from .language import Language
from .coverage import Coverage
from .unicode_set import UnicodeSet

class Report(object):

    def __init__(self, characters, language_filepath):
        self.language_filepath = language_filepath
        self.characters = self._maybe_make_set(characters)
        self.language = Language.parse(language_filepath)

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

    @property
    def complete(self):
        return not self.uncovered

    @property
    def incomplete(self):
        return not self.complete

    def _maybe_make_set(self, iterable):
        if not isinstance(iterable, set):
            iterable = UnicodeSet(iterable)
        return iterable
