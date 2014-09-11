import os
from smorgasbord.report import Report
from smorgasbord.language import Language
from smorgasbord.coverage import Coverage

path = os.path.dirname(os.path.abspath(__file__))
fixtures_path = os.path.join(path, 'fixtures')

def make_report():
    return Report([], os.path.join(fixtures_path, 'multiline.txt'))

class TestReport(object):

    def test_sets_language(self):
        report = make_report()
        assert hasattr(report, 'language')
        assert isinstance(report.language, Language)

    def test_sets_coverage(self):
        report = make_report()
        assert hasattr(report, 'coverage')
        assert isinstance(report.coverage, Coverage)
