from __future__ import unicode_literals
import unittest

import twingly_search

class ErrorsTest(unittest.TestCase):
    def test_from_api_response_message(self):
        with self.assertRaises(twingly_search.TwinglyAuthException):
            twingly_search.TwinglyException().from_api_response_message('... API key ...')

        with self.assertRaises(twingly_search.TwinglyServerException):
            twingly_search.TwinglyException().from_api_response_message('server error')

    def test_all_error_classes(self):
        error_classes = [
            twingly_search.TwinglyServerException,
            twingly_search.TwinglyAuthException,
            twingly_search.TwinglyQueryException
        ]

        for error_class in error_classes:
            with self.assertRaises(error_class):
                raise error_class()
