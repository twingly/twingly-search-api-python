#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

import requests

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

    def execute_query(self, q):
        """
        Executes the given search query and returns the result

        :param q: the search query to be executed
        :return: Result
        """
        response_body = self._get_response(q).content
        return Parser().parse(response_body)

    def _env_api_key(self):
        return os.environ.get('TWINGLY_SEARCH_KEY')

    def _get_response(self, q):
        query_string = self._build_query_string(q)
        response = self._session.get(query_string)
        return response

    def _build_query_string(self, q):
        search_parameters = self._url_parameters(q)
        query_string = "%s?%s" % (self.API_URL, search_parameters)
        return query_string

    def _url_parameters(self, q):
        """
        :return: the query part of the request url
        """
        parameters = {
            'q': q,
            'apiKey': self.api_key
        }
        return urlencode(parameters)
