#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

import requests

from twingly_search.errors import *
from twingly_search.search import Search

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


from twingly_search import __version__


class Client(object):
    """
    Twingly Search API client

    Attributes:
        search          (Search instance) Twingly Search API client instance
    """
    def __init__(self, api_key=None, user_agent='Twingly Search Python Client/%s'):
        """

        :param api_key: (string) Twingly Search API Key
        :param user_agent: (string) User Agent for client
        """

        if api_key is None:
            api_key = os.environ.get('TWINGLY_SEARCH_KEY')

        if api_key is None:
            raise TwinglyAuthException()

        self._api_key = api_key

        self._user_agent = user_agent
        if self._user_agent == 'Twingly Search Python Client/%s':
            self._user_agent = self._user_agent % (__version__)

        self.search = Search(self)

    def _request(self, method, url, params, user_agent=None):
        if 'key' not in params:
            params['key'] = self._api_key

        headers = {'User-Agent': self._user_agent}
        if user_agent is not None:
            headers = {'User-Agent': user_agent}

        response = requests.request(method, url, headers=headers, params=params)

        if 200 <= response.status_code < 300:
            try:
                doc = ET.XML(response.content)
            except Exception:
                raise TwinglyServerException(response.content)

            if doc.tag == 'html':
                raise TwinglyServerException(response.content)

            if doc.find('{http://www.twingly.com}operationResult') is not None:
                if doc.find('{http://www.twingly.com}operationResult').attrib['resultType'] == 'failure':
                    if 'API key' in doc.find('{http://www.twingly.com}operationResult').text:
                        raise TwinglyAuthException(doc.find('{http://www.twingly.com}operationResult').text)
                    else:
                        raise TwinglyServerException(doc.find('{http://www.twingly.com}operationResult').text)

            return doc
        else:
            if response.status_code >= 500:
                raise TwinglyServerException(response.content)
            else:
                raise TwinglyQueryException(response.content)