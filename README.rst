Smörgåsbord
===========

.. image:: https://travis-ci.org/jackjennings/smorgasbord.svg?branch=master
    :target: https://travis-ci.org/jackjennings/smorgasbord

Works like this:

.. code-block:: python

    from smorgasbord import Smorgasbord

    bord = Smorgasbord([97, "b", "c", u"ü", u"\u0660"])
    # => Smorgasbord([u"a", u"c", u"b", u"\xfc", u"\u0660"])

    en = bord.reports["en"]
    en.language.code
    # => "en"
    en.language.name
    # => "English"
    en.language.characters
    # => [u"a", u"b", u"c", ...]
    en.coverage
    # => 0.057
    en.coverage.percent
    # => u"5.7%"
    en.covered
    # => [u"a", u"b", u"c"]
    en.uncovered
    # => [u"d", u"e", u"f", ...]

Tested and working on Python 2.6, 2.7, 3.3, and 3.4.

Supported Languages
-------------------

* `English <smorgasbord/languages/en.txt>`_

Custom langauges files can be set at runtime by supplying a path to a folder:

.. code-block:: python

    Smorgasbord.language_paths.append("/my/path/to/language/files/dir")

Language Files
--------------

Each language is defined in a text file. Characters are separated by spaces, and lines starting with a ``#`` are ignored as comments. Line breaks can and should be used to wrap lines to 80 characters maximum.

For example, the ``en.txt`` definition for English:

.. code-block:: python

  # Language: English
  a b c d e f g h i j k l m n o p q r s t u v w x y z
  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

The first line is a special comment that will be parsed as the language name. Other special comments may be added in the future, but for now only ``Language`` is supported.

Contributing or Updating Languages
----------------------------------

1. Fork this repository
2. Add your language text file or modify and existing file
3. Commit the change with a brief description (e.g. ``created en.txt``, ``added ñ to es.txt``)
4. Create a pull request

Roadmap
-------

This is a quick list of features that will need to be added in the near future (and will probably comprise a 1.0 release).

* Lazily evaluate reports. Currently the library loads all language files when a Smorgasbord is initialized, which will get slow, fast. This should happen at the latest possible moment.
* Unicode ranges in language files. Adding support for unicode ranges will probably be necesary for languages with large character sets.
* Better language support. Probably starting with languages using the latin alphabet, and continue in subjective order of easiest to define and number of speakers.
