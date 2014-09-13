from os.path import splitext, basename
from itertools import takewhile

class LanguageParser(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self.code = splitext(basename(filepath))[0]
        self.characters = self.parse_characters()
        self.headers = self.parse_headers()
        self.name = self.headers.get('Language')

    def parse_characters(self):
        with open(self.filepath) as f:
            characters = [char for line in f if not self._is_comment(line)
                               for char in line.rstrip('\n').split(' ')]
        return characters

    def _is_comment(self, line):
        return line[0] == '#'

    def parse_headers(self):
        headers = {}
        with open(self.filepath) as f:
            head = takewhile(self._is_comment, f)
            for l in head:
                (key, value) = l[2:].split(':')
                headers[key.lower()] = value.strip()
        return headers
