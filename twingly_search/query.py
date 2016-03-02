import datetime
from pytz import utc

from twingly_search.errors import TwinglyQueryException

try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class Query(object):
    """
    Twingly Search API Query

    Attributes:
        pattern    (string) pattern the search query
        language   (string) language which language to restrict the query to
        client     (Client) the client that this query is connected to
        start_time (datetime.datetime) search for posts published after this time (inclusive)
                   Assumes UTC if the datetime object has no timezone set
        end_time   (datetime.datetime) search for posts published before this time (inclusive)
                   Assumes UTC if the datetime object has no timezone set
    """

    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, client):
        """
        No need to call this method manually, instead use Client#query.

        :param client: the client that this query should be connected to
        """
        self.client = client
        self.pattern = ''
        self.language = ''
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

    def url(self):
        """
        :return: request url for the query
        """
        return "%s?%s" % (self.client.endpoint_url(), self.url_parameters())

    def execute(self):
        """
        Executes the Query and returns the result

        :return: the Result for this query
        :raises TwinglyQueryException: if pattern is empty
        :raises TwinglyAuthException: if the API couldn't authenticate you
            Make sure your API key is correct
        :raises TwinglyServerException: if the query could not be executed
            due to a server error
        """
        return self.client.execute_query(self)

    def url_parameters(self):
        """
        :return: the query part of the request url
        """
        return urlencode(self.request_parameters())

    def request_parameters(self):
        """
        :return: the request parameters
        :raises TwinglyQueryException: if pattern is empty
        """
        if len(self.pattern) == 0:
            raise TwinglyQueryException("Missing pattern")

        return {
            'key': self.client.api_key,
            'searchpattern': self.pattern,
            'documentlang': self.language,
            'ts': self._time_to_utc_string(self.start_time),
            'tsTo': self._time_to_utc_string(self.end_time),
            'xmloutputversion': 2
        }

    def _time_to_utc_string(self, time):
        if time is None:
            return ''

        time_in_utc = self._time_to_utc(time)

        return time_in_utc.strftime(self.DATETIME_FORMAT)

    def _time_to_utc(self, time):
        if time.tzinfo is None:
            return time

        return time.astimezone(utc)

    def _assert_valid_time(self, time):
        if time is None:
            return

        if not isinstance(time, datetime.datetime):
            raise TwinglyQueryException("Not a datetime object")
