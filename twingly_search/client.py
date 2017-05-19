#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

import requests

from twingly_search.constants import TWINGLY_SEARCH_KEY
from twingly_search.query import Query

try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from twingly_search import __version__
from twingly_search.errors import *
from twingly_search.parser import Parser


class Client(object):
    """
    Twingly Search API client
    """

    BASE_URL = "https://api.twingly.com"
    SEARCH_API_VERSION = "v3"
    SEARCH_PATH = "/blog/search/api/%s/search" % SEARCH_API_VERSION
    API_URL = "%s%s" % (BASE_URL, SEARCH_PATH)
    DEFAULT_USER_AGENT = "Twingly Search Python Client/%s" % __version__

    def __init__(self, api_key=None, user_agent=None):
        """
        :param api_key: (string) Twingly Search API Key
        :param user_agent: (string) the user agent to be used for
            all API requests
        """

        if api_key is None:
            api_key = self._env_api_key()

        if api_key is None:
            raise TwinglySearchException("No API key has been provided.")

        self.api_key = api_key

        self._user_agent = user_agent
        if self._user_agent is None:
            self._user_agent = self.DEFAULT_USER_AGENT

        self._session = requests.Session()
        self._session.headers.update({'User-Agent': self._user_agent})

    def query(self):
        """
        Returns a new Query object connected to this client

        :return: Query
        """
        return Query(self)

    def execute_query(self, q):
        """
        Executes the given search query and returns the result

        :param q: the search query to be executed
        :type q: unicode | str | Query
        :return: Result
        """
        query_string = self._get_query_string(q)
        response_body = self._get_response(query_string).content
        result = Parser().parse(response_body)
        return result

    def _get_query_string(self, q):
        if self._is_string(q):
            return q
        return q.build_query_string()

    @staticmethod
    def _is_string(q):
        try:
            return isinstance(q, (str, unicode))
        except NameError:
            # python 3
            return isinstance(q, str)

    @staticmethod
    def _env_api_key():
        return os.environ.get(TWINGLY_SEARCH_KEY)

    def _get_response(self, q):
        """
        Make request with query string and return response
        :param q: query string
        :type q: str
        :return: response
        :rtype requests.Response
        """
        query_url = self._build_query_url(q)
        response = self._session.get(query_url)
        return response

    def _build_query_url(self, q):
        url_parameters = self._url_parameters(q)
        query_url = "%s?%s" % (self.API_URL, url_parameters)
        return query_url

    def endpoint_url(self):
        """
        :return: API endpoint URL
        """
        return self.API_URL

    def _url_parameters(self, q):
        """
        :return: the query part of the request url
        """
        parameters = {
            'q': q,
            'apiKey': self.api_key
        }
        return urlencode(parameters)
