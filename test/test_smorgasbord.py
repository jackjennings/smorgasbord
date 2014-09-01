from smorgasbord import Smorgasbord


class TestSmorgasbord(object):

    def test_init_converts_to_unicode(self):
        s = Smorgasbord(['a'])
        assert s.pop() == u"a"

    def test_init_converts_integer_to_unicode(self):
        s = Smorgasbord([97])
        assert s.pop() == u"a"

    def test_contains_integer_representation(self):
        s = Smorgasbord(['a'])
        assert 97 in s

    def test_contains_chr_representation(self):
        s = Smorgasbord([u'a'])
        assert 'a' in s
