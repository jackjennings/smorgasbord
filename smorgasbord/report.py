from __future__ import division
import os
from .language import Language
from .coverage import Coverage
from .unicode_set import UnicodeSet

class Report(object):

    def __init__(self, characters, language_file):
        self.characters = UnicodeSet(characters)
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
