class UrlKeyExistsException(Exception):

    def __init__(self, url_key=None):
        self.message = f'Url key already exists.'
        self.url_key = url_key
        super().__init__(self.message)


class LocationNotFoundException(Exception):

    def __init__(self):
        self.message = f'Sorry the given address was not found.'
        super().__init__(self.message)
