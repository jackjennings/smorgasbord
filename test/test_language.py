import os
from smorgasbord.language import Language
from smorgasbord.unicode_set import UnicodeSet

path = os.path.dirname(os.path.abspath(__file__))
fixtures_path = os.path.join(path, 'fixtures')

class TestLanguage(object):

    def test_parse(self):
        lang = Language.parse(os.path.join(fixtures_path, 'multiline.txt'))
        assert isinstance(lang, Language)
        assert "Foo" == lang.name
        assert UnicodeSet(['a', 'b', 'c']) == lang.characters
