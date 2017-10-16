from __future__ import unicode_literals

import unittest
from datetime import datetime

import dateutil.parser
import pytz
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
        self.assertIn("q=christmas", q.url())

    def test_query_without_valid_pattern(self):
        with self.assertRaises(twingly_search.TwinglySearchQueryException):
            q = self._client.query()
            q.url()

    def test_query_with_empty_pattern(self):
        with self.assertRaises(twingly_search.TwinglySearchQueryException):
            q = self._client.query()
            q.pattern = ""
            q.url()

    def test_query_should_return_new_parameters_for_deprecated_ones(self):
        q = self._client.query()
        q.pattern = "spotify"
        self.assertEqual(q.pattern, q.search_query)

    def test_query_should_add_language(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.language = "en"
        self.assertIn("lang:en", q.build_query_string())

    def test_query_should_add_start_date(self):
        q = self._client.query()
        q.search_query = "spotify"
        q.start_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "UTC")
        query_string = q.build_query_string()
        self.assertEqual(query_string, "spotify start-date:2012-12-28 09:01:22")

    def test_query_should_add_end_date(self):
        q = self._client.query()
        q.search_query = "spotify"
        q.end_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "UTC")
        query_string = q.build_query_string()
        self.assertEqual(query_string, "spotify end-date:2012-12-28 09:01:22")

    def test_query_should_add_lang(self):
        q = self._client.query()
        q.search_query = "spotify"
        q.language = "en"
        query_string = q.build_query_string()
        self.assertEqual(query_string, "spotify lang:en")

    def test_query_should_build_query_string_with_deprecated_params(self):
        q = self._client.query()
        q.search_query = "spotify"
        q.language = "en"
        q.start_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "UTC")
        q.end_time = self.datetime_with_timezone(datetime(2013, 12, 28, 9, 1, 22), "UTC")
        query_string = q.build_query_string()
        self.assertEqual(query_string,
                         "spotify lang:en start-date:2012-12-28 09:01:22 end-date:2013-12-28 09:01:22")

    def test_query_should_build_query_string(self):
        q = self._client.query()
        q.search_query = "spotify"
        q.language = "en"
        q.start_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "UTC")
        q.end_time = self.datetime_with_timezone(datetime(2013, 12, 28, 9, 1, 22), "UTC")
        query_string = q.build_query_string()
        self.assertEqual(query_string,
                         "spotify lang:en start-date:2012-12-28 09:01:22 end-date:2013-12-28 09:01:22")

    def test_query_should_add_start_time(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.start_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "UTC")
        self.assertIn("start-date:2012-12-28 09:01:22", q.build_query_string())

    def test_query_using_start_time_without_timezone(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.start_time = datetime(2012, 12, 28, 9, 1, 22)
        self.assertIn("start-date:2012-12-28 09:01:22", q.build_query_string())

    def test_query_using_start_time_with_timezone_other_than_utc(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.start_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "Europe/Stockholm")
        self.assertIn("start-date:2012-12-28 08:01:22", q.build_query_string())

    def test_query_using_start_time_parsed_by_dateutil(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.start_time = dateutil.parser.parse("2012-12-28 09:01:22 -0800")
        self.assertIn("start-date:2012-12-28 17:01:22", q.build_query_string())

    def test_query_when_start_time_is_not_a_datetime(self):
        q = self._client.query()
        with self.assertRaises(twingly_search.TwinglySearchQueryException):
            q.start_time = "This is not a datetime object"

    def test_query_should_add_end_time(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.end_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "UTC")
        self.assertIn("end-date:2012-12-28 09:01:22", q.build_query_string())

    def test_query_using_end_time_without_timezone(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.end_time = datetime(2012, 12, 28, 9, 1, 22)
        self.assertIn("end-date:2012-12-28 09:01:22", q.build_query_string())

    def test_query_using_end_time_with_timezone_other_than_utc(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.end_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "Europe/Stockholm")
        self.assertIn("end-date:2012-12-28 08:01:22", q.build_query_string())

    def test_query_using_end_time_parsed_by_dateutil(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.end_time = dateutil.parser.parse("2012-12-28 09:01:22 +0800")
        self.assertIn("2012-12-28 01:01:22", q.build_query_string())

    def test_query_when_end_time_is_not_a_datetime(self):
        q = self._client.query()
        with self.assertRaises(twingly_search.TwinglySearchQueryException):
            q.end_time = "This is not a datetime object"

    def test_query_should_encode_url_parameters(self):
        q = self._client.query()
        q.pattern = "spotify"
        q.end_time = self.datetime_with_timezone(datetime(2012, 12, 28, 9, 1, 22), "UTC")
        self.assertIn("end-date%3A2012-12-28+09%3A01%3A22", q.url_parameters())

    def test_query_pattern(self):
        q = self._client.query()
        q.pattern = "spotify"
        self.assertIn("q=spotify", q.url_parameters())

    def test_query_when_searching_for_spotify(self):
        with Betamax(self._client._session).use_cassette('search_for_spotify_on_sv_blogs_from_query'):
            q = self._client.query()
            q.pattern = "spotify page-size:10"
            q.language = "sv"
            result = q.execute()
            self.assertIsNotNone(result)
            self.assertEqual(result.incomplete_result, False)
            self.assertEqual(result.number_of_matches_returned, 10)
            self.assertEqual(len(result.posts), 10)
