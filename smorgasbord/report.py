import os
from .language import Language

class Report(object):
    
    def __init__(self, bord, language_file):
        self.code = os.path.splitext(os.path.basename(language_file))[0]
