# coding: utf-8

from __future__ import unicode_literals

import unittest

import twingly_search
from twingly_search import Post


class ParserTest(unittest.TestCase):
    def get_fixture(self, fixture_name):
        file_path = "./tests./fixtures/%s.xml" % fixture_name
        fixture = open(file_path, 'r').read()
        return fixture

    def assert_blog_posts_equal(self, actual_post, expected_post):
        self.assertEqual(actual_post.id, expected_post.id)
        self.assertEqual(actual_post.author, expected_post.author)
        self.assertEqual(actual_post.url, expected_post.url)
        self.assertEqual(actual_post.title, expected_post.title)
        self.assertEqual(actual_post.text, expected_post.text)
        self.assertEqual(actual_post.language_code, expected_post.language_code)
        self.assertEqual(actual_post.location_code, expected_post.location_code)
        self.assertEqual(actual_post.coordinates, expected_post.coordinates)
        self.assertEqual(actual_post.links, expected_post.links)
        self.assertEqual(actual_post.tags, expected_post.tags)
        self.assertEqual(actual_post.images, expected_post.images)
        self.assertEqual(actual_post.indexed_at, expected_post.indexed_at)
        self.assertEqual(actual_post.published_at, expected_post.published_at)
        self.assertEqual(actual_post.reindexed_at, expected_post.reindexed_at)
        self.assertEqual(actual_post.inlinks_count, expected_post.inlinks_count)
        self.assertEqual(actual_post.blog_id, expected_post.blog_id)
        self.assertEqual(actual_post.blog_name, expected_post.blog_name)
        self.assertEqual(actual_post.blog_url, expected_post.blog_url)
        self.assertEqual(actual_post.blog_rank, expected_post.blog_rank)
        self.assertEqual(actual_post.authority, expected_post.authority)

    #     TODO assert each post data
    def test_with_incomplete_result(self):
        data = self.get_fixture("incomplete_result")
        r = twingly_search.Parser().parse(data)

        self.assertIsInstance(r, twingly_search.Result)
        self.assertEqual(len(r.posts), 0)
        self.assertEqual(r.number_of_matches_total, 0)
        self.assertEqual(r.number_of_matches_returned, 0)
        self.assertEqual(r.seconds_elapsed, 0.203)
        self.assertEqual(r.incomplete_result, True)

    def test_with_minimal_valid_result(self):
        data = self.get_fixture("minimal_valid_result")
        r = twingly_search.Parser().parse(data)
        self.assertIsInstance(r, twingly_search.Result)
        posts = r.posts
        self.assertEqual(len(posts), 3)
        self.assertEqual(r.number_of_matches_total, 3122050)
        self.assertEqual(r.number_of_matches_returned, 3)
        self.assertEqual(r.seconds_elapsed, 0.369)
        self.assertEqual(r.incomplete_result, False)

        first_expected_post = Post()

    def test_with_valid_empty_result(self):
        data = self.get_fixture("valid_empty_result")
        r = twingly_search.Parser().parse(data)
        self.assertIsInstance(r, twingly_search.Result)
        self.assertEqual(len(r.posts), 0)
        self.assertEqual(r.number_of_matches_total, 0)
        self.assertEqual(r.number_of_matches_returned, 0)
        self.assertEqual(r.seconds_elapsed, 0.203)
        self.assertEqual(r.incomplete_result, False)

    def test_with_nonexistent_api_key_result(self):
        with self.assertRaises(twingly_search.TwinglySearchClientException) as cm:
            data = self.get_fixture("nonexistent_api_key_result")
            r = twingly_search.Parser().parse(data)
        ex = cm.exception
        error = ex.error
        self.assertEqual(error.code, '40001')
        self.assertEqual(error.message, 'Parameter apikey may not be empty')

    def test_with_unauthorized_api_key_result(self):
        with self.assertRaises(twingly_search.TwinglySearchClientException) as cm:
            data = self.get_fixture("unauthorized_api_key_result")
            r = twingly_search.Parser().parse(data)
        ex = cm.exception
        error = ex.error
        self.assertEqual(error.code, '40101')
        self.assertEqual(error.message, 'Unauthorized')

    def test_with_service_unavailable_result(self):
        with self.assertRaises(twingly_search.TwinglySearchServerException) as cm:
            data = self.get_fixture("service_unavailable_result")
            r = twingly_search.Parser().parse(data)
        ex = cm.exception
        error = ex.error
        self.assertEqual(error.code, '50301')
        self.assertEqual(error.message, 'Authentication service unavailable')

    def test_with_undefined_error_result(self):
        with self.assertRaises(twingly_search.TwinglySearchServerException) as cm:
            data = self.get_fixture("undefined_error_result")
            r = twingly_search.Parser().parse(data)
        ex = cm.exception
        error = ex.error
        self.assertEqual(error.code, '50001')
        self.assertEqual(error.message, 'Internal Server Error')

    def test_with_non_xml_result(self):
        with self.assertRaises(twingly_search.TwinglySearchException):
            data = self.get_fixture("non_xml_result")
            r = twingly_search.Parser().parse(data)
