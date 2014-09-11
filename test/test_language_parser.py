import os
from smorgasbord.language_parser import LanguageParser

path = os.path.dirname(os.path.abspath(__file__))
fixtures_path = os.path.join(path, 'fixtures')

class TestLanguageParser(object):

    def test_parses_code(self):
        parser = LanguageParser(os.path.join(fixtures_path, 'multiline.txt'))
        assert parser.code == 'multiline'
