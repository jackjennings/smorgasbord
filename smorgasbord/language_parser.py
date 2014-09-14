import codecs
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
        with self._open_file() as f:
            characters = [char for line in f if not self._is_comment(line)
                               for char in line.rstrip('\n').split(' ')]
        return characters

    def parse_headers(self):
        headers = {}
        with self._open_file() as f:
            head = takewhile(self._is_header, f)
            for line in head:
                (key, value) = self._split_header(line)
                headers[key.lower()] = value.strip()
        return headers

    def _split_header(self, line):
        return line[2:].split(':')

    def _is_comment(self, line):
        return line[0] == '#'
    
    def _is_header(self, line):
        return self._is_comment(line) and line.find(':') != -1

    def _open_file(self):
        return codecs.open(self.filepath, "r", "utf-8")
