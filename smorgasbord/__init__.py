import os
from .smorgasbord import Smorgasbord

__version__ = "0.0.1"

path = os.path.dirname(os.path.abspath(__file__))
Smorgasbord.language_paths.append(os.path.join(path, 'languages'))
