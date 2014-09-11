from __future__ import division
import os
from .language import Language
from .unicode_set import UnicodeSet
from .coverage import Coverage

class Report(object):

    def __init__(self, bord, language_file):
        self.language = Language.parse(language_file)
        self.coverage = Coverage(len(self.covered) / len(self.uncovered))

    @property
    def code(self):
        return self.language.code

    @property
    def covered(self):
        return UnicodeSet([])

    @property
    def uncovered(self):
        return UnicodeSet(['f'])
