import datetime
from pytz import utc

class Post(object):
    """
    A blog post

    Attributes:
        url           (string) the post URL
        title         (string) the post title
        summary       (string) the blog post text
        language_code (string) ISO two letter language code for the language that the post was written in
        published     (datetime.datetime) the time, in UTC, when this post was published
        indexed       (datetime.datetime) the time, in UTC, when this post was indexed by Twingly
        blog_url      (string) the blog URL
        blog_name     (string) name of the blog
        blog_rank     (int) the rank of the blog, based on authority and language
                      (https://developer.twingly.com/resources/search/#authority)
        authority     (int) the blog's authority/influence
                      (https://developer.twingly.com/resources/search/#authority)
        tags          (list of string) tags
    """

    def __init__(self):
        self.url = ''
        self.title = ''
        self.summary = ''
        self.language_code = ''
        self.published = self._parse_time("1970-01-01 00:00:00Z")
        self.indexed = self._parse_time("1970-01-01 00:00:00Z")
        self.blog_url = ''
        self.blog_name = ''
        self.authority = 0
        self.blog_rank = 0
        self.tags = []

    def set_values(self, params):
        """
        Sets all instance variables for the Post, given a dict.

        :param params: (dict) containing blog post data
        """
        self.url = params['url']
        self.title = params['title']
        self.summary = params['summary']
        self.language_code = params['languageCode']
        self.published = self._parse_time(params['published'])
        self.indexed = self._parse_time(params['indexed'])
        self.blog_url = params['blogUrl']
        self.blog_name = params['blogName']
        self.authority = int(params['authority'])
        self.blog_rank = int(params['blogRank'])
        self.tags = params['tags']

    def _parse_time(self, time):
        parsed_time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%SZ')
        return utc.localize(parsed_time)

    def __unicode__(self):
        return "%s %s" % (self.title, self.url)

    def __str__(self):
        return self.__unicode__()
