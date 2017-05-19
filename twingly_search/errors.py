from __future__ import division
from __future__ import unicode_literals


class Error(object):
    """
    Error response from the Search API
    
    Attributes:
        code    (string) error code
        message (string) error message
    """

    def __init__(self, code='', message=''):
        self.code = code
        self.message = message

    def __unicode__(self):
        return "Error code: %s. Error message: %s." % (self.code, self.message)

    def __str__(self):
        return self.__unicode__()


class TwinglySearchException(Exception):
    @classmethod
    def from_api_response_message(cls, error):
        """
        Create TwinglySearchException from the Error
        :param error: error from the API response
        """
        if error is not None and error.code is not None:
            if error.code.startswith('4'):
                if error.code.startswith('400') or error.code.startswith('404'):
                    raise TwinglySearchQueryException(error)
                if error.code.startswith('401') or error.code.startswith('402'):
                    raise TwinglySearchAuthenticationException(error)
                raise TwinglySearchClientException(error)
            if error.code.startswith('5'):
                raise TwinglySearchServerException(error)
            raise TwinglySearchErrorException(error)


class TwinglySearchErrorException(TwinglySearchException):
    def __init__(self, error):
        super(TwinglySearchErrorException, self).__init__(str(error))
        self.error = error


class TwinglySearchServerException(TwinglySearchErrorException):
    pass


class TwinglySearchClientException(TwinglySearchErrorException):
    pass


class TwinglySearchQueryException(TwinglySearchClientException):
    pass


class TwinglySearchAuthenticationException(TwinglySearchClientException):
    pass
