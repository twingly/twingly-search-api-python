class TwinglyException(Exception):
    def from_api_response_message(self, message):
        """
        :param message: API response error message
        """
        if 'API key' in message:
            raise TwinglyAuthException(message)
        else:
            raise TwinglyServerException(message)


class TwinglyAuthException(TwinglyException):
    pass


class TwinglyServerException(TwinglyException):
    pass


class TwinglyQueryException(TwinglyException):
    pass
