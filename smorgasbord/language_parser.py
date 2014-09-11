from os.path import splitext, basename

class LanguageParser(object):

    def __init__(self, language_file):
        self.code = splitext(basename(language_file))[0]
        self.name = 'Foo'
        self.characters = []
