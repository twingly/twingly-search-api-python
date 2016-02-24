from __future__ import unicode_literals
import unittest
from datetime import datetime
import pytz
import dateutil.parser
from betamax import Betamax
import twingly_search

class QueryTest(unittest.TestCase):
    def setUp(self):
        self._client = twingly_search.Client()

    def datetime_with_timezone(self, date, timezone_string):
        timezone = pytz.timezone(timezone_string)
        return timezone.localize(date)

    def test_query_new(self):
        q = self._client.query()
        self.assertIsInstance(q, twingly_search.Query)

    def test_query_without_client(self):
        with self.assertRaises(Exception):
            q = twingly_search.Query()

    def test_query_with_valid_pattern(self):
        q = self._client.query()
        q.pattern = "christmas"
        self.assertIn("xmloutputversion=2", q.url())

    def test_query_without_valid_pattern(self):
        with self.assertRaises(twingly_search.TwinglyQueryException):
            q = self._client.query()
            q.url()

    def test_query_with_empty_pattern(self):
        with self.assertRaises(twingly_search.TwinglyQueryException):
            q = self._client.query()
            q.pattern = ""
            q.url()

    def test_query_should_add_language(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.language = "en"
        self.assertEqual(q.request_parameters()['documentlang'], "en")

    def test_query_should_add_start_time(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.start_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "UTC")
        self.assertEqual(q.request_parameters()['ts'], "2012-12-28 09:01:22")

    def test_query_using_start_time_without_timezone(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.start_time = datetime(2012, 12, 28, 9, 1, 22)
        self.assertEqual(q.request_parameters()['ts'], "2012-12-28 09:01:22")

    def test_query_using_start_time_with_timezone_other_than_utc(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.start_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "Europe/Stockholm")
        self.assertEqual(q.request_parameters()['ts'], "2012-12-28 08:01:22")

    def test_query_using_start_time_parsed_by_dateutil(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.end_time = dateutil.parser.parse("2012-12-28 09:01:22 -0800")
        self.assertEqual(q.request_parameters()['tsTo'], "2012-12-28 17:01:22")

    def test_query_should_add_end_time(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.end_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "UTC")
        self.assertEqual(q.request_parameters()['tsTo'], "2012-12-28 09:01:22")

    def test_query_using_end_time_without_timezone(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.end_time = datetime(2012, 12, 28, 9, 1, 22)
        self.assertEqual(q.request_parameters()['tsTo'], "2012-12-28 09:01:22")

    def test_query_using_end_time_with_timezone_other_than_utc(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.end_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "Europe/Stockholm")
        self.assertEqual(q.request_parameters()['tsTo'], "2012-12-28 08:01:22")

    def test_query_using_end_time_parsed_by_dateutil(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.end_time = dateutil.parser.parse("2012-12-28 09:01:22 +0800")
        self.assertEqual(q.request_parameters()['tsTo'], "2012-12-28 01:01:22")

    def test_query_should_encode_url_parameters(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.end_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "UTC")
        self.assertIn("tsTo=2012-12-28+09%3A01%3A22", q.url_parameters())

    def test_query_pattern(self):
        q = self._client.query()
        q.pattern = "spotify"
        self.assertIn("searchpattern=spotify", q.url_parameters())

    def test_query_when_searching_for_spotify(self):
        with Betamax(self._client._session).use_cassette('search_for_spotify_on_sv_blogs'):
            q = self._client.query()
            q.pattern = "spotify page-size:10"
            q.language = "sv"
            r = q.execute()
            self.assertGreater(len(r.posts), 0)
