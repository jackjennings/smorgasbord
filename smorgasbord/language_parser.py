import codecs
from os.path import splitext, basename
from itertools import takewhile
from unicodeset import UnicodeSet


class LanguageParser(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self.code = splitext(basename(filepath))[0]
        self.headers = self._parse_headers()
        self.characters = self._parse_characters()
        self.name = self.headers.get('language')

    def _parse_headers(self):
        headers = {}
        for line in self._header_lines():
            (key, value) = self._split_header(line)
            headers[key.lower()] = value.strip()
        return headers

    def _parse_characters(self):
        characters = [char for line in self._codepoint_lines()
                           for char in self._parse_line_characters(line)]
        return UnicodeSet(characters)

    def _parse_line_characters(self, line):
        return [char for sequence in line.rstrip('\n').split(' ')
                     for char in self._parse_sequence_characters(sequence)]

    def _parse_sequence_characters(self, sequence):
        components = sequence.split('-')
        if len(components) is 1:
            return components
        else:
            return range(ord(components[0]), ord(components[1]) + 1)

    def _header_lines(self):
        with self._open_file() as f:
            return list(takewhile(self._is_header, f))

    def _codepoint_lines(self):
        with self._open_file() as f:
            return [line for line in f if not self._is_comment(line)]

    def _split_header(self, line):
        return line[2:].split(':')

    def _is_comment(self, line):
        return line[0] == '#'
    
    def _is_header(self, line):
        return self._is_comment(line) and line.find(':') != -1

    def _open_file(self):
        return codecs.open(self.filepath, "r", "utf-8")
