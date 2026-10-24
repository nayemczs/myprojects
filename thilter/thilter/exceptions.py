class UrlKeyExistsException(Exception):

    def __init__(self, url_key=None):
        self.message = f'Url key already exists.'
        self.url_key = url_key
        super().__init__(self.message)
