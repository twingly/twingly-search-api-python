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

    Attributes:
        search          (Search instance) Twingly Search API client instance
    """

    BASE_URL = "https://api.twingly.com"
    SEARCH_PATH = "/analytics/Analytics.ashx"
    DEFAULT_USER_AGENT = "Twingly Search Python Client/%s"

    def __init__(self, api_key=None, user_agent=None):
        """

        :param api_key: (string) Twingly Search API Key
        :param user_agent: (string) User Agent for client
        """

        if api_key is None:
            api_key = self.env_api_key()

        if api_key is None:
            raise TwinglyAuthException()

        self.api_key = api_key

        self._user_agent = user_agent
        if self._user_agent is None:
            self._user_agent = self.DEFAULT_USER_AGENT % __version__

    def query(self):
        return Query(self)

    def execute_query(self, query):
        response_body = self.get_response(query).content
        return Parser().parse(response_body)

    def endpoint_url(self):
        return "%s%s" % (self.BASE_URL, self.SEARCH_PATH)

    def env_api_key(self):
        return os.environ.get('TWINGLY_SEARCH_KEY')

    def get_response(self, query):
        headers = {'User-Agent': self._user_agent}
        response = requests.get(query.url(), headers=headers, proxies={'http': '127.0.0.1:8888','https': '127.0.0.1:8888'}, verify=False)
        if 200 <= response.status_code < 300:
            return response
        else:
            if response.status_code >= 500:
                raise TwinglyServerException(response.content)
            else:
                raise TwinglyQueryException(response.content)

    def api_key_missing(self):
        raise TwinglyAuthException("No API key has been provided.")
