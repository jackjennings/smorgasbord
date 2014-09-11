from smorgasbord import Smorgasbord


class TestSmorgasbord(object):

    def test_has_reports(self):
        bord = Smorgasbord(['a'])
        assert hasattr(bord, 'reports')

    def test_has_language_paths(self):
        assert hasattr(Smorgasbord, 'language_paths')

    def test_can_add_language_paths(self):
        Smorgasbord.language_paths.append('foo')
        assert 'foo' in Smorgasbord.language_paths
        Smorgasbord.language_paths.pop()
