import os
from smorgasbord.language_parser import LanguageParser

path = os.path.dirname(os.path.abspath(__file__))
fixtures_path = os.path.join(path, 'fixtures')

def make_parser(filename):
    return LanguageParser(os.path.join(fixtures_path, filename))

class TestLanguageParser(object):

    def test_parses_code(self):
        parser = make_parser('multiline.txt')
        assert parser.code == 'multiline'

    def test_parses_characters(self):
        parser = make_parser('basic.txt')
        assert [u"a", u"b", u"c"] == list(parser.characters)

    def test_parses_characters_from_multiple_lines(self):
        parser = make_parser('multiline.txt')
        assert [u"a", u"b", u"c"] == list(parser.characters)

    def test_parses_unicode_characters(self):
        parser = make_parser("unicode.txt")
        assert [u"d", u"\xdf", u"\xe5", u"\xe7"] == list(parser.characters)

    def test_parses_headers(self):
        parser = make_parser('basic.txt')
        assert {"language": "Foo"} == parser.headers

    def test_parses_language(self):
        parser = make_parser('basic.txt')
        assert "Foo" == parser.name

    def test_parses_headers_with_extra_comments(self):
        parser = make_parser('extra_header_comments.txt')
        assert {"language": "Foo"} == parser.headers

    def test_parses_chracters_with_extra_comments(self):
        parser = make_parser('extra_comments.txt')
        assert [u"a", u"b", u"c"] == list(parser.characters)

    def test_parses_ranges(self):
        parser = make_parser('ranges.txt')
        assert [u"a", u"b", u"c", u"d", u"e", u"f"] == list(parser.characters)
