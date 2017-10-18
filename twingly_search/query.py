import datetime

import deprecation
from pytz import utc

import twingly_search
from twingly_search.constants import QUERY_DATE_TIME_FORMAT
from twingly_search.errors import TwinglySearchQueryException

try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class Query(object):
    """
    Twingly Search API Query

    Attributes:
        search_query (string) the search query
        language     (string) which language to restrict the query to
        client       (Client) the client that this query is connected to
        start_time   (datetime.datetime) search for posts published after this time (inclusive)
                     Assumes UTC if the datetime object has no timezone set
        end_time     (datetime.datetime) search for posts published before this time (inclusive)
                     Assumes UTC if the datetime object has no timezone set
    """

    def __init__(self, client):
        """
        No need to call this method manually, instead use Client#query.

        :param client: the client that this query should be connected to
        :type client: twingly_search.Client
        """
        self.client = client
        self.search_query = ''
        self._language = ''
        self._start_time = None
        self._end_time = None

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, time):
        self._assert_valid_time(time)
        self._start_time = time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, time):
        self._assert_valid_time(time)
        self._end_time = time

    def build_query_string(self):
        """
        Build search query in string representation from the current Query object
        :return: search query
        :rtype str
        """
        full_search_query = self.search_query
        if self._language:
            full_search_query += " lang:" + self._language
        if self.start_time:
            full_search_query += " start-date:" + self._time_to_utc_string(self.start_time)
        if self.end_time:
            full_search_query += " end-date:" + self._time_to_utc_string(self.end_time)
        return full_search_query

    @property
    @deprecation.deprecated(deprecated_in="2.0.0", removed_in="3.0.0", current_version=twingly_search.__version__,
                            details="Language is part of search query now. Use 'lang:value' in search_query instead.")
    def language(self):
        return self._language

    @language.setter
    @deprecation.deprecated(deprecated_in="2.0.0", removed_in="3.0.0", current_version=twingly_search.__version__,
                            details="Language is part of search query now. Use 'lang:value' in search_query instead.")
    def language(self, value):
        self._language = value

    @property
    @deprecation.deprecated(deprecated_in="2.0.0", removed_in="3.0.0", current_version=twingly_search.__version__,
                            details="Use 'search_query' field instead")
    def pattern(self):
        return self.search_query

    @pattern.setter
    @deprecation.deprecated(deprecated_in="2.0.0", removed_in="3.0.0", current_version=twingly_search.__version__,
                            details="Use 'search_query' field instead")
    def pattern(self, value):
        self.search_query = value

    @deprecation.deprecated(deprecated_in="2.0.0", removed_in="3.0.0", current_version=twingly_search.__version__,
                            details="Use Client directly with build_query_string function instead.")
    def url(self):
        """
        :return: request url for the query
        """
        return "%s?%s" % (self.client.endpoint_url(), self.url_parameters())

    @deprecation.deprecated(deprecated_in="2.0.0", removed_in="3.0.0", current_version=twingly_search.__version__,
                            details="Use Client directly with build_query_string function instead.")
    def execute(self):
        """
        Executes the Query and returns the result

        :return: the Result for this query
        :raises TwinglySearchQueryException: if search_query is empty
        :raises TwinglySearchAuthenticationException: if the API couldn't authenticate you
            Make sure your API key is correct
        :raises TwinglySearchServerException: if the query could not be executed
            due to a server error
        """
        return self.client.execute_query(self.build_query_string())

    @deprecation.deprecated(deprecated_in="2.0.0", removed_in="3.0.0", current_version=twingly_search.__version__,
                            details="Use Client directly with build_query_string function instead.")
    def url_parameters(self):
        """
        :return: the query part of the request url
        """
        return urlencode(self.request_parameters())

    @deprecation.deprecated(deprecated_in="2.0.0", removed_in="3.0.0", current_version=twingly_search.__version__,
                            details="Use Client directly with build_query_string function instead.")
    def request_parameters(self):
        """
        :return: the request parameters
        :raises TwinglySearchQueryException: if search_query is empty
        """
        if len(self.search_query) == 0:
            raise TwinglySearchQueryException("Missing search query")

        return {
            'apikey': self.client.api_key,
            'q': self.build_query_string()
        }

    def _time_to_utc_string(self, time):
        if time is None:
            return ''

        time_in_utc = self._time_to_utc(time)
        result = time_in_utc.strftime(QUERY_DATE_TIME_FORMAT)
        return result

    def _time_to_utc(self, time):
        if time.tzinfo is None:
            return time

        return time.astimezone(utc)

    def _assert_valid_time(self, time):
        if time is None:
            return

        if not isinstance(time, datetime.datetime):
            raise TwinglySearchQueryException("Not a datetime object")
