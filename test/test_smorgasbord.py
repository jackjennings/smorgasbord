import os
from smorgasbord import Smorgasbord

path = os.path.dirname(os.path.abspath(__file__))
fixtures_path = os.path.join(path, 'fixtures')

class TestSmorgasbord(object):

    def test_has_reports(self):
        bord = Smorgasbord(['a'])
        assert hasattr(bord, 'reports')

    def test_has_paths(self):
        assert hasattr(Smorgasbord, 'paths')

    def test_can_add_paths(self):
        Smorgasbord.paths.append('foo')
        assert 'foo' in Smorgasbord.paths
        Smorgasbord.paths.pop()

    def test_updates_reports_when_changed(self):
        Smorgasbord.paths.append(fixtures_path)
        bord = Smorgasbord(['a'])
        bord.add('b')
        assert ['a', 'b'] == [c for c in bord.reports['basic'].covered]
        Smorgasbord.paths.pop()
