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

    def test_without_api_key_at_all(self):
        with self.assertRaises(twingly_search.TwinglyAuthException):
            twingly_search.Client()