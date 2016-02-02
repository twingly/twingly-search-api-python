import datetime

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
            'ts': self._ts(),
            'tsTo': self._tsTo(),
            'xmloutputversion': 2
        }

    def _ts(self):
        if self.start_time is not None:
            if isinstance(self.start_time, datetime.datetime):
                return self.start_time.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(self.start_time, basestring):
                return self.start_time
            else:
                return ''
        else:
            return ''

    def _tsTo(self):
        if self.end_time is not None:
            if isinstance(self.end_time, datetime.datetime):
                return self.end_time.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(self.end_time, basestring):
                return self.end_time
            else:
                return ''
        else:
            return ''
