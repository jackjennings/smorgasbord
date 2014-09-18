import os
from smorgasbord import Smorgasbord

path = os.path.dirname(os.path.abspath(__file__))
fixtures_path = os.path.join(path, 'fixtures')

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

    def test_updates_reports_when_changed(self):
        Smorgasbord.language_paths.append(fixtures_path)
        bord = Smorgasbord(['a'])
        bord.add('b')
        assert ['a', 'b'] == [c for c in bord.reports['basic'].covered]
        Smorgasbord.language_paths.pop()
