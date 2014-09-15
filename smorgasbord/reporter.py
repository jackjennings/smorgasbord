import os
from .report import Report

class Reporter(object):

    def __init__(self, bord, paths):
        self.bord = bord
        self.language_files = [f for directory in paths
                                 for f in self._listdir(directory)]
        self.reports = {}
        for r in (Report(bord, f) for f in self.language_files):
            if not r.code in self.reports:
                self.reports[r.code] = r

    def _listdir(self, directory):
        return (os.path.join(directory, f) for f in os.listdir(directory))

    def __getitem__(self, key):
        return self.reports[key]
    
    def __contains__(self, item):
        return item in self.reports

    def __iter__(self):
        return iter(self.reports)
