#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

import requests

from twingly_search import __version__
from twingly_search.errors import *
from twingly_search.parser import Parser
from twingly_search.query import Query


class Client(object):
    """
    Twingly Search API client
    """

    BASE_URL = "https://api.twingly.com"
    SEARCH_PATH = "/analytics/Analytics.ashx"
    DEFAULT_USER_AGENT = "Twingly Search Python Client/%s"

    def __init__(self, api_key=None, user_agent=None):
        """
        :param api_key: (string) Twingly Search API Key
        :param user_agent: (string) the user agent to be used for
            all API requests
        """

        if api_key is None:
            api_key = self._env_api_key()

        if api_key is None:
            self._api_key_missing()

        self.api_key = api_key

        self._user_agent = user_agent
        if self._user_agent is None:
            self._user_agent = self.DEFAULT_USER_AGENT % __version__

        self._session = requests.Session()
        self._session.headers.update({'User-Agent': self._user_agent})

    def query(self):
        """
        Returns a new Query object connected to this client

        :return: Query
        """
        return Query(self)

    def execute_query(self, query):
        """
        Executes the given Query and returns the result

        :param query: the Query to be executed
        :return: Result
        """
        response_body = self._get_response(query).content
        return Parser().parse(response_body)

    def endpoint_url(self):
        """
        :return: API endpoint URL
        """
        return "%s%s" % (self.BASE_URL, self.SEARCH_PATH)

    def _env_api_key(self):
        return os.environ.get('TWINGLY_SEARCH_KEY')

    def _get_response(self, query):
        response = self._session.get(query.url())
        if 200 <= response.status_code < 300:
            return response
        else:
            if response.status_code >= 500:
                raise TwinglyServerException(response.content)
            else:
                raise TwinglyQueryException(response.content)

    def _api_key_missing(self):
        raise TwinglyAuthException("No API key has been provided.")
