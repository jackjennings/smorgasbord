Smörgåsbord
===========

.. image:: https://travis-ci.org/jackjennings/smorgasbord.svg?branch=master
    :target: https://travis-ci.org/jackjennings/smorgasbord

Smörgåsbord tests coverage over unicode character sets.

The ``Smorgasbord`` class inherits from ``UnicodeSet`` and supports `the same features <https://github.com/jackjennings/unicodeset>`_.

Supports Python 2.6 – 3.x

.. code-block:: bash

    $ pip install smorgasbord

.. code-block:: python

    from smorgasbord import Smorgasbord

    # Provide a path to a file or folder of character sets
    Smorgasbord.paths.prepend("/my/path/to/language/en.txt")

    >>> bord = Smorgasbord([97, "b", "c", u"ü", u"\u0660"])
    Smorgasbord([u"a", u"c", u"b", u"\xfc", u"\u0660"])

    # Reports are accessed though the "reports" dict using the language code
    >>> en = bord.reports["en"]
    
    # Basic information about the report's language is accessible
    >>> en.language.code
    "en"
    >>> en.language.name
    "English"
    >>> en.language.characters
    FrozenUnicodeSet([u"a", u"b", u"c", ...])
    
    # Amount of coverage is availbe as float and string representations
    >>> en.coverage
    0.057
    >>> en.coverage.percentage
    u"5.7%"
    
    # Sets of glyphs can be accessed
    >>> en.covered
    FrozenUnicodeSet([u"a", u"b", u"c"])
    >>> en.uncovered
    FrozenUnicodeSet([u"d", u"e", u"f", ...])
    
    # Reports can also return a boolean value for completeness:
    >>> en.complete
    False
    >>> en.incomplete
    True

Character Set Files
-------------------

Each character set is defined in a text file. Characters are separated by spaces, and lines starting with a ``#`` are ignored as comments. Line breaks can and should be used to wrap lines to 80 characters maximum.

For example, an ``en.txt`` definition for an English coverage character set:

.. code-block:: python

    # Language: English
    a b c d e f g h i j k l m n o p q r s t u v w x y z
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

The first line is a special comment that will be parsed as the language name. Other special comments may be added in the future, but for now only ``Language`` is supported.

Supplying Character Sets
------------------------

Character sets are made available by supplying a path to a folder, or directly to a language file.

.. code-block:: python

    Smorgasbord.paths.prepend("/my/path/to/language/files/dir")
    Smorgasbord.paths.prepend("/my/path/to/language/file.txt")

Character set files are searched for in each succesive folder, using the first matching file.

Alternatively, the ``paths`` array can be replaced entirely:

.. code-block:: python

    Smorgasbord.paths = ["/my/path/to/language/files/dir"]

Roadmap
-------

This is a quick list of features that will need to be added in the near future (and will probably comprise a 1.0 release).

* Lazily evaluate reports. Currently the library loads all language files when a Smorgasbord is initialized, which will get slow, fast. This should happen at the latest possible moment.
* Unicode ranges in language files. Adding support for unicode ranges will probably be necesary for languages with large character sets.
