from __future__ import unicode_literals
import unittest
import twingly_search
import os

class ClientTest(unittest.TestCase):
    def test_new(self):
        c = twingly_search.Client(os.environ.get('API_KEY'))
        self.assertEqual(c._user_agent, 'Twingly Search Python Client/%s' % (twingly_search.__version__))

    def test_without_api_key_as_parameter(self):
        os.environ['TWINGLY_SEARCH_KEY'] = os.environ.get('API_KEY')
        c = twingly_search.Client()
        self.assertEqual(c._user_agent, 'Twingly Search Python Client/%s' % (twingly_search.__version__))
        del os.environ['TWINGLY_SEARCH_KEY']

    def test_with_no_api_key_at_all(self):
        with self.assertRaises(twingly_search.TwinglyAuthException):
            twingly_search.Client()

    def test_with_optional_user_agent_given(self):
        c = twingly_search.Client(os.environ.get('API_KEY'), user_agent="Test User-Agent")
        self.assertEqual(c._user_agent, "Test User-Agent")

    def test_query(self):
        q = twingly_search.Client(os.environ.get('API_KEY')).query()
        self.assertIsInstance(q, twingly_search.Query)

    def test_execute_query_with_invalid_api_key(self):
        with self.assertRaises(twingly_search.TwinglyAuthException):
            c = twingly_search.Client('123')
            q = c.query()
            q.pattern = 'something'
            c.execute_query(q)

    def test_endpoint_url(self):
        self.assertEqual(twingly_search.Client(os.environ.get('API_KEY')).endpoint_url(), "%s%s" % (twingly_search.Client.BASE_URL, twingly_search.Client.SEARCH_PATH))