from . import api


class Client:

    def __init__(self, token):
        self.token = token
        self.api = api.API(self.token)
