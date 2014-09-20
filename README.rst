Smörgåsbord
===========

.. image:: https://travis-ci.org/jackjennings/smorgasbord.svg?branch=master
    :target: https://travis-ci.org/jackjennings/smorgasbord

Smörgåsbord tests sets of unicode characters to determine what language support is covered.

This library deveoped as a tool for type designers only as an approximate guide for planning purposes. `Regional <https://en.wikipedia.org/wiki/Serbian_Cyrillic_alphabet#Differences_from_other_Cyrillic_alphabets>`_ `variation <https://en.wikipedia.org/wiki/Regional_handwriting_variation>`_ in `letterforms <https://en.wikipedia.org/wiki/Han_unification>`_ is left as a exercise for the designer, and detection isn't a planned feature.

The ``Smorgasbord`` class inherits from ``UnicodeSet`` and supports `the same features <https://github.com/jackjennings/unicodeset>`_.

Supports Python 2.6 – 3.x

.. code-block:: bash

    $ pip install smorgasbord

.. code-block:: python

    from smorgasbord import Smorgasbord

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

Supported Languages
-------------------

* `English <smorgasbord/languages/en.txt>`_

Language Files
--------------

Each language is defined in a text file. Characters are separated by spaces, and lines starting with a ``#`` are ignored as comments. Line breaks can and should be used to wrap lines to 80 characters maximum.

For example, the ``en.txt`` definition for English:

.. code-block:: python

    # Language: English
    a b c d e f g h i j k l m n o p q r s t u v w x y z
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

The first line is a special comment that will be parsed as the language name. Other special comments may be added in the future, but for now only ``Language`` is supported.

Custom Language Files
---------------------

Custom langauges files can be set at runtime by supplying a path to a folder, or directly to a language file.

.. code-block:: python

    Smorgasbord.language_paths.prepend("/my/path/to/language/files/dir")
    Smorgasbord.language_paths.prepend("/my/path/to/language/file.txt")

Language files are searched for in each succesive folder, using the first matching file. Language files included with this package can be overriden by prepending a local folder; an ``en.txt`` language file in the local folder will be used in preference to the internal ``en.txt``.

Alternatively, the ``language_paths`` array can be replaced to only use locally available language files:

.. code-block:: python

    Smorgasbord.language_paths = ["/my/path/to/language/files/dir"]

Contributing
------------

1. `Fork <https://github.com/jackjennings/smorgasbord/fork>`_ this repository
2. Add your language file to the `languages directory <smorgasbord/languages>`_ or modify an existing file
3. Add you language to the `list of supported languages <jackjennings/smorgasbord#supported-languages>`_ in this README
4. Commit the change with a brief description (e.g. ``created en.txt``, ``added ñ to es.txt``)
5. Create a pull request

Roadmap
-------

This is a quick list of features that will need to be added in the near future (and will probably comprise a 1.0 release).

* Lazily evaluate reports. Currently the library loads all language files when a Smorgasbord is initialized, which will get slow, fast. This should happen at the latest possible moment.
* Unicode ranges in language files. Adding support for unicode ranges will probably be necesary for languages with large character sets.
* Better language support. Probably starting with languages using the latin alphabet, and continue in subjective order of easiest to define and number of speakers.
