from __future__ import division
import os
from .language import Language
from .coverage import Coverage
from unicodeset import FrozenUnicodeSet


class Report(object):

    def __init__(self, characters, reference_filepath):
        self.characters = self._maybe_make_set(characters)
        self.reference_filepath = reference_filepath
        self.reference = Language.parse(reference_filepath)

    @property
    def coverage(self):
        return Coverage(len(self.covered) / len(self.reference.characters))

    @property
    def code(self):
        return self.reference.code

    @property
    def covered(self):
        return FrozenUnicodeSet(self.reference.characters & self.characters)

    @property
    def uncovered(self):
        return FrozenUnicodeSet(self.reference.characters - self.characters)

    @property
    def complete(self):
        return not self.uncovered

    @property
    def incomplete(self):
        return not self.complete

    @property
    def language(self):
        import warnings
        warnings.warn("The `language` property has been renamed to \
                      `reference` and will be removed in version 1.0",
                      DeprecationWarning)
        return self.reference

    def _maybe_make_set(self, iterable):
        if not isinstance(iterable, set) or isinstance(iterable, frozenset):
            iterable = FrozenUnicodeSet(iterable)
        return iterable
