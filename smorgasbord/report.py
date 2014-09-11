import os
from .language import Language

class Report(object):

    def __init__(self, bord, language_file):
        self.language = Language.parse(language_file)

    @property
    def code(self):
        return self.language.code
