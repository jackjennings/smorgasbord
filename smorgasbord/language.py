from .language_parser import LanguageParser
from unicodeset import FrozenUnicodeSet


class Language(object):
    
    @classmethod
    def parse(cls, language_file):
        parser = LanguageParser(language_file)
        return cls(parser.code, parser.characters, parser.headers)
        
    def __init__(self, code, characters=None, headers=None):
        self.code = code
        self.headers = headers
        self.name = self.headers.get('language')
        self.characters = FrozenUnicodeSet(characters)
