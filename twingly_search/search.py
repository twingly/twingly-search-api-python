#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

from twingly_search.errors import *


class Result(object):
    """
    Represents a result from a query to the Search API

    Attributes:
        number_of_matches_returned  (int) number of Post the query returned
        number_of_matches_total     (int) total number of Post the query matched
        seconds_elapsed             (float) number of seconds it took to execute the query
        posts                       (list of Post) all posts that matched the query
    """
    def __init__(self, doc):
        """
        :param response: (string) response from Twingly API
        :param version: (int)version of returned XML
        """

        self.number_of_matches_returned = int(doc.attrib['numberOfMatchesReturned'])
        self.seconds_elapsed = float(doc.attrib['secondsElapsed'])
        self.number_of_matches_total = int(doc.attrib['numberOfMatchesTotal'])

        self.posts = []

        for p in doc.findall('post'):
            post = Post(p)
            if post.content_type == 'blog':
                self.posts.append(post)

    def all_results_returned(self):
        """
        :return: (boolean) returns True if this result includes all Posts that matched the query
        """
        return self.number_of_matches_total == self.number_of_matches_returned

    def __unicode__(self):
        return "Number of matches returned: %d Seconds elapsed: %.3f Number of matches total: %d" % (self.number_of_matches_returned, self.seconds_elapsed, self.number_of_matches_total)

    def __str__(self):
        return self.__unicode__()


class Post(object):
    """
    A blog post

    Attributes:
         content_type   (string)
         url            (string) url the post URL
         title          (string) title the post title
         summary        (string) summary the blog post text
         language_code  (string) language_code ISO two letter language code for the language that the post was written in
         blog_url       (string) blog_url the blog URL
         blog_name      (string) blog_name name of the blog
         blog_rank      (int) the rank of the blog, based on authority and language (https://developer.twingly.com/resources/search/#authority)
         authority      (int) authority the blog's authority/influence (https://developer.twingly.com/resources/search/#authority)
         published      (datetime.datetime) published the time, in UTC, when this post was published
         indexed        (datetime.datetime) indexed the time, in UTC, when this post was indexed by Twingly
         tags           (list of string) tags
    """
    def __init__(self, post, version=0):
        """
        :param post: (xml.Element) post content
        :param version: (int) version of XML
        :return:
        """
        self.content_type = post.attrib['contentType']
        if self.content_type == 'blog':
            self.url = post.find('url').text
            self.title = post.find('title').text
            self.summary = post.find('summary').text
            self.language_code = post.find('languageCode').text
            self.blog_url = post.find('blogUrl').text
            self.blog_name = post.find('blogName').text
            self.blog_rank = 0
            self.authority = int(post.find('authority').text)
            self.published = datetime.datetime.strptime("1970-01-01 00:00:00Z", '%Y-%m-%d %H:%M:%SZ')
            self.indexed = datetime.datetime.strptime("1970-01-01 00:00:00Z", '%Y-%m-%d %H:%M:%SZ')
            self.tags = []

            self.content_type = post.get('contentType')
            self.published = datetime.datetime.strptime(post.find('published').text, '%Y-%m-%d %H:%M:%SZ')
            self.indexed = datetime.datetime.strptime(post.find('indexed').text, '%Y-%m-%d %H:%M:%SZ')

            if post.find('tags') is not None:
                for tag in post.find('tags'):
                    self.tags.append(tag.text)

            self.blog_rank = int(post.find('blogRank').text)

    def __unicode__(self):
        return "%s %s" % (self.title, self.url)

    def __str__(self):
        return self.__unicode__()

class Query(object):
    """
    Twingly Search API Query

    Attributes:
        pattern     (string) pattern the search query
        language    (string) language which language to restrict the query to
        start_time  (datetime.datetime) search for posts published after this time (inclusive)
        end_time    (datetime.datetime) search for posts published before this time (inclusive)
        endpoint    (string) Twingly Search API endpoint
    """
    def __init__(self, pattern, client, language=None, start_time=None, end_time=None):
        self.pattern = pattern
        self.language = language
        self.start_time = start_time
        self.end_time = end_time
        self._client = client
        self.endpoint = 'https://api.twingly.com/analytics/Analytics.ashx'

    def execute(self):
        """
        Executes Query and returns Result object

        :return: Result object
        """
        if self.pattern == '' or self.pattern is None:
            raise TwinglyQueryException('Missing pattern')

        params = {
            'searchpattern': self.pattern,
            'xmloutputversion': 2
        }

        if self.language is not None:
            params['documentlang'] = self.language

        if self.start_time is not None:
            if isinstance(self.start_time, datetime.datetime):
                params['ts'] = self.start_time.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(self.start_time, basestring):
                params['ts'] = self.start_time

        if self.end_time is not None:
            if isinstance(self.end_time, datetime.datetime):
                params['tsTo'] = self.end_time.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(self.end_time, basestring):
                params['tsTo'] = self.end_time

        doc = self._client._request('GET', self.endpoint, params)
        return Result(doc)

class Search(object):
    """
    API methods holder
    """
    def __init__(self, client):
        self._client = client

    def query(self, pattern, language=None, start_time=None, end_time=None):
        """
        Twingly Search API query

        :param pattern: (string) pattern the search query
        :param language: (string) language which language to restrict the query to
        :param start_time: (datetime.datetime) search for posts published after this time (inclusive)
        :param end_time: (datetime.datetime) search for posts published before this time (inclusive)
        :return:
        """
        return Query(pattern, self._client, language, start_time, end_time)


