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
        pattern     (string) pattern the search query
        language    (string) language which language to restrict the query to
        client      (Client) the client that this query is connected to
        start_time  (datetime.datetime) search for posts published after this time (inclusive)
        end_time    (datetime.datetime) search for posts published before this time (inclusive)
    """
    pattern = ''
    language = ''
    client = None
    start_time = None
    end_time = None

    def __init__(self, client):
        """
        No need to call this method manually, instead use {Client#query}.

        :param client: the client that this query should be connected to
        """
        self.client = client

    def url(self):
        """
        :return: request url for the query
        """
        return "%s?%s" % (self.client.endpoint_url(), self.url_parameters())

    def execute(self):
        """
        Executes the query and returns the result
        :return: the result for this query
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
        """
        if len(self.pattern) == 0:
            raise TwinglyQueryException("Missing pattern")

        return {
            'key': self.client.api_key,
            'searchpattern': self.pattern,
            'documentlang': self.language,
            'ts': self._time_to_utc_string(self.start_time, "start_time"),
            'tsTo': self._time_to_utc_string(self.end_time, "end_time"),
            'xmloutputversion': 2
        }

    def _time_to_utc_string(self, time, attr_name):
        if time is not None:
            if isinstance(time, datetime.datetime):
                if time.tzinfo is None:
                    raise TwinglyQueryException("No timezone set for %s" % attr_name)
                return time.astimezone(utc).strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(time, basestring):
                return time
            else:
                return ''
        else:
            return ''
