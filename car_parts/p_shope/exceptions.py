class InsufficientQuantityException(Exception):

    def __init__(self):
        self.message = f'Sorry, the requested amount is not available.'
        super().__init__(self.message)
