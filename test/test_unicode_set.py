from smorgasbord.unicode_set import UnicodeSet


class TestUnicodeSet(object):

    def test_init_converts_to_unicode(self):
        s = UnicodeSet(['a'])
        assert s.pop() == u"a"

    def test_init_converts_integer_to_unicode(self):
        s = UnicodeSet([97])
        assert s.pop() == u"a"

    def test_contains_integer_representation(self):
        s = UnicodeSet(['a'])
        assert 97 in s

    def test_contains_chr_representation(self):
        s = UnicodeSet([u'a'])
        assert 'a' in s
