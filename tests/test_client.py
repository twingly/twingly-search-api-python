from __future__ import unicode_literals

import os
import unittest

from betamax import Betamax

import twingly_search
from twingly_search.constants import TWINGLY_SEARCH_KEY


class ClientTest(unittest.TestCase):
    def test_new(self):
        c = twingly_search.Client("test-key")
        self.assertEqual(c._user_agent, 'Twingly Search Python Client/%s' % (twingly_search.__version__))

    def test_query(self):
        q = twingly_search.Client().query()
        self.assertIsInstance(q, twingly_search.Query)

    def test_without_api_key_as_parameter(self):
        c = twingly_search.Client()
        self.assertEqual(c.api_key, os.environ.get(TWINGLY_SEARCH_KEY))

    def test_with_no_api_key_at_all(self):
        temp_key = os.environ.get(TWINGLY_SEARCH_KEY)
        del os.environ[TWINGLY_SEARCH_KEY]
        with self.assertRaises(twingly_search.TwinglySearchException):
            twingly_search.Client()
        os.environ[TWINGLY_SEARCH_KEY] = temp_key

    def test_with_optional_user_agent_given(self):
        c = twingly_search.Client(user_agent="Test User-Agent")
        self.assertEqual(c._user_agent, "Test User-Agent")

    def test_execute_query_with_invalid_api_key(self):
        temp_key = os.environ.get(TWINGLY_SEARCH_KEY)
        os.environ[TWINGLY_SEARCH_KEY] = 'wrong'
        c = twingly_search.Client()

        with Betamax(c._session).use_cassette('search_without_valid_api_key'):
            with self.assertRaises(twingly_search.TwinglySearchException):
                q = 'something'
                c.execute_query(q)

        os.environ[TWINGLY_SEARCH_KEY] = temp_key

    def test_search_for_spotify_on_sv_blogs(self):
        c = twingly_search.Client()

        with Betamax(c._session).use_cassette('search_for_spotify_on_sv_blogs'):
            q = 'spotify page-size:10 lang:sv'
            result = c.execute_query(q)
            self.assertIsNotNone(result)
            self.assertEqual(result.incomplete_result, False)
            self.assertEqual(result.number_of_matches_returned, 10)
            self.assertEqual(len(result.posts), 10)
