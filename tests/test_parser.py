# coding: utf-8

from __future__ import unicode_literals
import unittest

import twingly_search

class ParserTest(unittest.TestCase):
    def get_fixture(self, fixture_name):
        file_path = "./tests/fixtures/%s.xml" % fixture_name
        fixture = open(file_path, 'r').read()
        return fixture

    def assert_blog_posts_equal(self, actual_post, expected_post):
        self.assertEqual(actual_post.url, expected_post.url)
        self.assertEqual(actual_post.title, expected_post.title)
        self.assertEqual(actual_post.summary, expected_post.summary)
        self.assertEqual(actual_post.language_code, expected_post.language_code)
        self.assertEqual(actual_post.published, expected_post.published)
        self.assertEqual(actual_post.indexed, expected_post.indexed)
        self.assertEqual(actual_post.blog_url, expected_post.blog_url)
        self.assertEqual(actual_post.blog_name, expected_post.blog_name)
        self.assertEqual(actual_post.blog_rank, expected_post.blog_rank)
        self.assertEqual(actual_post.authority, expected_post.authority)
        self.assertEqual(actual_post.tags, expected_post.tags)

    def test_with_valid_result(self):
        data = self.get_fixture("valid_result")
        r = twingly_search.Parser().parse(data)
        self.assertIsInstance(r, twingly_search.Result)

    def test_with_valid_result_containing_non_blogs(self):
        data = self.get_fixture("valid_non_blog_result")
        r = twingly_search.Parser().parse(data)
        self.assertIsInstance(r, twingly_search.Result)
        self.assertEqual(len(r.posts), 1)

    def test_with_nonexistent_api_key_result(self):
        with self.assertRaises(twingly_search.TwinglyAuthException):
            data = self.get_fixture("nonexistent_api_key_result")
            r = twingly_search.Parser().parse(data)

    def test_with_unauthorized_api_key_result(self):
        with self.assertRaises(twingly_search.TwinglyAuthException):
            data = self.get_fixture("unauthorized_api_key_result")
            r = twingly_search.Parser().parse(data)

    def test_with_service_unavailable_result(self):
        with self.assertRaises(twingly_search.TwinglyServerException):
            data = self.get_fixture("service_unavailable_result")
            r = twingly_search.Parser().parse(data)

    def test_with_undefined_error_result(self):
        with self.assertRaises(twingly_search.TwinglyServerException):
            data = self.get_fixture("undefined_error_result")
            r = twingly_search.Parser().parse(data)

    def test_with_undefined_error_result(self):
        with self.assertRaises(twingly_search.TwinglyServerException):
            data = self.get_fixture("non_xml_result")
            r = twingly_search.Parser().parse(data)

    def test_with_post_containing_one_tag(self):
        fixture = self.get_fixture("minimal_valid_result")
        result = twingly_search.Parser().parse(fixture)

        expected_values = {
             "url": "http://oppogner.blogg.no/1409602010_bare_m_ha.html",
             "title": "Bare MÅ ha!",
             "summary": "Ja, velkommen til høsten ...",
             "languageCode": "no",
             "published": "2014-09-02 06:53:26Z",
             "indexed": "2014-09-02 09:00:53Z",
             "blogUrl": "http://oppogner.blogg.no/",
             "blogName": "oppogner",
             "authority": "1",
             "blogRank": "1",
             "tags": ["Blogg"],
        }

        expected_post = twingly_search.Post()
        expected_post.set_values(expected_values)
        actual_post = result.posts[0]

        self.assert_blog_posts_equal(actual_post, expected_post)

    def test_with_post_containing_multiple_tags(self):
        fixture = self.get_fixture("minimal_valid_result")
        result = twingly_search.Parser().parse(fixture)

        expected_values = {
             "url": "http://www.skvallernytt.se/hardtraning-da-galler-swedish-house-mafia",
             "title": "Hårdträning – då gäller Swedish House Mafia",
             "summary": """Träning. Och Swedish House Mafia. Det verkar vara ett lyckat koncept. "Don't you worry child" och "Greyhound" är nämligen de två mest spelade träningslåtarna under januari 2013 på Spotify.

Relaterade inlägg:
Swedish House Mafia – ny låt!
Ny knivattack på Swedish House Mafia-konsert
Swedish House Mafia gör succé i USA""",
             "languageCode": "sv",
             "published": "2013-01-29 15:21:56Z",
             "indexed": "2013-01-29 15:22:52Z",
             "blogUrl": "http://www.skvallernytt.se/",
             "blogName": "Skvallernytt.se",
             "authority": "38",
             "blogRank": "4",
             "tags": ["Okategoriserat", "Träning", "greyhound", "koncept", "mafia"],
        }

        expected_post = twingly_search.Post()
        expected_post.set_values(expected_values)
        actual_post = result.posts[1]

        self.assert_blog_posts_equal(actual_post, expected_post)

    def test_with_post_containing_no_tags(self):
        fixture = self.get_fixture("minimal_valid_result")
        result = twingly_search.Parser().parse(fixture)

        expected_values = {
             "url": "http://didriksinspesielleverden.blogg.no/1359472349_justin_bieber.html",
             "title": "Justin Bieber",
             "summary": """OMG! Justin Bieber Believe acoustic albumet er nå ute på spotify. Han er helt super. Love him. Personlig liker jeg best beauty and a beat og as long as you love me, kommenter gjerne hva dere synes! <3 #sus YOLO""",
             "languageCode": "no",
             "published": "2013-01-29 15:12:29Z",
             "indexed": "2013-01-29 15:14:37Z",
             "blogUrl": "http://didriksinspesielleverden.blogg.no/",
             "blogName": "Didriksinspesielleverden",
             "authority": "0",
             "blogRank": "1",
             "tags": [],
        }

        expected_post = twingly_search.Post()
        expected_post.set_values(expected_values)
        actual_post = result.posts[2]

        self.assert_blog_posts_equal(actual_post, expected_post)
