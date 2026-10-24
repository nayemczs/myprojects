from settings.settings import MIN_ARTICLE_LENGTH


class ArticleTooSmallException(Exception):

    def __init__(self):
        self.message = f'Article must be minimum of: {MIN_ARTICLE_LENGTH} characters'
        super().__init__(self.message)
