import os
from smorgasbord.reporter import Reporter
from smorgasbord.report import Report

path = os.path.dirname(os.path.abspath(__file__))
fixtures_path = os.path.join(path, 'fixtures')

class TestReporter(object):

    def test_sets_bord(self):
        reporter = Reporter(['a'], [fixtures_path])
        assert hasattr(reporter, 'bord')
        assert reporter.bord == ['a']

    def test_finds_language_files(self):
        reporter = Reporter(['a'], [fixtures_path])
        assert hasattr(reporter, 'language_files')
        assert os.path.join(fixtures_path, 'multiline.txt') in \
            reporter.language_files

    def test_gets_reports(self):
        reporter = Reporter(['a'], [fixtures_path])
        assert hasattr(reporter, 'reports')

    def test_sets_reports(self):
        reporter = Reporter(['a'], [fixtures_path])
        assert reporter.reports['multiline']

    def test_reports_directly_accessible(self):
        reporter = Reporter(['a'], [fixtures_path])
        assert reporter['multiline']

    def test_reports_allow_containment_check(self):
        reporter = Reporter(['a'], [fixtures_path])
        assert 'multiline' in reporter

    def test_reports_return_report_objects(self):
        reporter = Reporter(['a'], [fixtures_path])
        assert isinstance(reporter['multiline'], Report)

    def test_reporter_iter(self):
        reporter = Reporter([], [fixtures_path])
        keys = [key for key in reporter]
        expects = ['basic', 'multiline', 'unicode']
        for e in expects:
            assert e in keys
