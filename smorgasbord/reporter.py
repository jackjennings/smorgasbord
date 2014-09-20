import os
from .report import Report


class Reporter(object):

    def __init__(self, bord, paths):
        self.bord = bord
        self.language_files = self._get_language_files(paths)
        self.reports = self._make_reports(self.language_files)

    def __getitem__(self, key):
        return self.reports[key]
    
    def __contains__(self, item):
        return item in self.reports

    def __iter__(self):
        return iter(self.reports)

    def _get_language_files(self, paths):
        return [f for path in paths for f in self._get_files(path)]

    def _make_reports(self, files):
        reports = {}
        for r in (Report(self.bord, f) for f in files):
            if not r.code in reports:
                reports[r.code] = r
        return reports

    def _get_files(self, path):
        if os.path.isdir(path):
            return self._list_dir(path)
        else:
            return [path]

    def _list_dir(self, directory):
        return (os.path.join(directory, f) for f in os.listdir(directory))
