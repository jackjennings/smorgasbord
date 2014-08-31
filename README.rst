Smörgåsbord
===========

Probably will work something like this:

.. code-block:: python

    from smorgasbord import Smorgasbord

    spread = Smorgasbord([97, "b", "c", u"ü", u"\u0660"])

    english = spread.reports['en']
    english.language.name
    # => "English"
    english.language.characters
    # => [u"a", u"b", u"c", ...]
    english.coverage
    # => 0.057
    english.coverage.percent
    # => u"5.7%"
    english.covered
    # => [u"a", u"b", u"c"]
    english.uncovered
    # => [u"d", u"e", u"f", ...]

    all = [report for reports in spread.reports]
    # => [<Report lang="en">, <Report lang="fr">, ...]
