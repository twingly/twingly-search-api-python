from __future__ import unicode_literals

import unittest

from twingly_search.errors import *


class ErrorsTest(unittest.TestCase):
    def test_from_api_response_message(self):
        with self.assertRaises(TwinglySearchClientException):
            code = '40501'
            message = 'message'
            error = Error(code, message)
            TwinglySearchException.from_api_response_message(error)

        with self.assertRaises(TwinglySearchAuthenticationException):
            code = '40101'
            message = 'message'
            error = Error(code, message)
            TwinglySearchException.from_api_response_message(error)

        with self.assertRaises(TwinglySearchAuthenticationException):
            code = '40201'
            message = 'message'
            error = Error(code, message)
            TwinglySearchException.from_api_response_message(error)

        with self.assertRaises(TwinglySearchQueryException):
            code = '40000'
            message = 'message'
            error = Error(code, message)
            TwinglySearchException.from_api_response_message(error)

        with self.assertRaises(TwinglySearchQueryException):
            code = '40400'
            message = 'message'
            error = Error(code, message)
            TwinglySearchException.from_api_response_message(error)

        with self.assertRaises(TwinglySearchServerException):
            code = '50101'
            message = 'message'
            error = Error(code, message)
            TwinglySearchException.from_api_response_message(error)

        with self.assertRaises(TwinglySearchErrorException):
            code = '10101'
            message = 'message'
            error = Error(code, message)
            TwinglySearchException.from_api_response_message(error)

    def test_all_error_classes(self):
        error_classes = [
            TwinglySearchClientException,
            TwinglySearchServerException,
            TwinglySearchErrorException,
            TwinglySearchException,
            TwinglySearchQueryException,
            TwinglySearchAuthenticationException
        ]

        for error_class in error_classes:
            with self.assertRaises(error_class):
                code = 'code'
                message = 'message'
                error = Error(code, message)
                raise error_class(error)
