from .language_parser import LanguageParser
from unicodeset import FrozenUnicodeSet


class Language(object):
    
    @classmethod
    def parse(cls, language_file):
        parser = LanguageParser(language_file)
        return cls(parser.code, parser.headers['language'], parser.characters)
        
    def __init__(self, code, name, characters=None, qualifiers=None):
        self.code = code
        self.name = name
        self.characters = FrozenUnicodeSet(characters)
