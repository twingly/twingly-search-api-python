import datetime

class Post(object):
    """
    A blog post

    Attributes:
         url            (string) the post URL
         title          (string) the post title
         summary        (string) the blog post text
         language_code  (string) ISO two letter language code for the language that the post was written in
         published      (datetime.datetime) published the time, in UTC, when this post was published
         indexed        (datetime.datetime) indexed the time, in UTC, when this post was indexed by Twingly
         blog_url       (string) the blog URL
         blog_name      (string) name of the blog
         blog_rank      (int) the rank of the blog, based on authority and language
                        (https://developer.twingly.com/resources/search/#authority)
         authority      (int) authority the blog's authority/influence
                        (https://developer.twingly.com/resources/search/#authority)
         tags           (list of string) tags
    """
    url = ''
    title = ''
    summary = ''
    language_code = ''
    published = datetime.datetime.strptime("1970-01-01 00:00:00Z", '%Y-%m-%d %H:%M:%SZ')
    indexed = datetime.datetime.strptime("1970-01-01 00:00:00Z", '%Y-%m-%d %H:%M:%SZ')
    blog_url = ''
    blog_name = ''
    authority = 0
    blog_rank = 0
    tags = []

    def set_values(self, params):
        """
        Sets all instance variables for the Post, given a dict.

        :param params: (dict) containing blog post data
        """
        self.url = params['url']
        self.title = params['title']
        self.summary = params['summary']
        self.language_code = params['languageCode']
        self.published = datetime.datetime.strptime(params['published'], '%Y-%m-%d %H:%M:%SZ')
        self.indexed = datetime.datetime.strptime(params['indexed'], '%Y-%m-%d %H:%M:%SZ')
        self.blog_url = params['blogUrl']
        self.blog_name = params['blogName']
        self.authority = int(params['authority'])
        self.blog_rank = int(params['blogRank'])
        self.tags = params['tags']

    def __unicode__(self):
        return "%s %s" % (self.title, self.url)

    def __str__(self):
        return self.__unicode__()
