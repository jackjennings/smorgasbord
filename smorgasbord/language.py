from .language_parser import LanguageParser
from .unicode_set import UnicodeSet

class Language(object):
    
    @classmethod
    def parse(cls, language_file):
        parser = LanguageParser(language_file)
        return cls(parser.code, parser.name, parser.characters)
        
    def __init__(self, code, name, characters=[], qualifiers=[]):
        self.code = code
        self.name = name
        self.characters = UnicodeSet(['a', 'b', 'c'])
