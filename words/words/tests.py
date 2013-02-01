from django.test import TestCase


class WordsTest(TestCase):
    """
    This seems too simple to test. I wouldn't be testing domain logic, just
    wiring.

    /<iso-code>/<int>/              - Get back that many words, one per line.
    /<iso-code>/<int>/?profane=true - Get back that many words, possibly
                                      including profanity.

    Extenions: join-character, min word length, max worth length, special
    word lists.
    """
