import os
from smorgasbord.report import Report
from smorgasbord.language import Language
from smorgasbord.coverage import Coverage

path = os.path.dirname(os.path.abspath(__file__))
fixtures_path = os.path.join(path, 'fixtures')

def make_report(chars=None):
    if chars is None:
        chars = []
    return Report(chars, os.path.join(fixtures_path, 'basic.txt'))

class TestReport(object):

    def test_sets_language(self):
        report = make_report()
        assert hasattr(report, 'language')
        assert isinstance(report.reference, Language)

    def test_sets_coverage(self):
        report = make_report()
        assert hasattr(report, 'coverage')
        assert isinstance(report.coverage, Coverage)

    def test_returns_incomplete(self):
        report = make_report()
        assert report.incomplete

    def test_returns_complete(self):
        report = make_report()
        report = make_report(report.reference.characters)
        assert report.complete
