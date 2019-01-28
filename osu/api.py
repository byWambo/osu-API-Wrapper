import requests
from .models import *


class API:

    def __init__(self, token):
        self.token = token
        self.base_url = 'https://osu.ppy.sh'

    def get_beatmaps(self, since=None, mode=0, limit=500):
        params = dict(k=self.token)
        if since:
            params.update({"since": since})
        params.update({"m": mode, "limit": limit})
        r = requests.get(self.base_url + '/api/get_beatmaps', params=params)
        try:
            _return = list()
            for bp in r.json():
                _return.insert(0, beatmap.Beatmap(bp))
            return _return
        except IndexError:
            return None

    def get_user(self, name: str, mode=0):
        params = dict(k=self.token)
        params.update({"m": mode, "u": name})
        r = requests.get(self.base_url + '/api/get_user', params=params)
        try:
            return user.User(r.json()[0])
        except IndexError:
            return None

    def get_scores(self, beatmap_id: int, username=None, mode=0, limit=50):
        params = dict(k=self.token)
        if username:
            params.update({"u": username, "type": "string"})
        params.update({"b": beatmap_id, "m": mode, "limit": limit})
        r = requests.get(self.base_url + '/api/get_user', params=params)
        print(r.json())

    def get_user_best(self, username: str, mode=0, limit=10):
        params = dict(k=self.token)
        if username:
            params.update({"u": username, "type": "string"})
        params.update({"m": mode, "limit": limit})
        r = requests.get(self.base_url + '/api/get_user_best', params=params)
        try:
            return user.UserBest(r.json()[0])
        except IndexError:
            return None

    def get_user_recent(self, username: str, mode=0, limit=10):
        params = dict(k=self.token)
        if username:
            params.update({"u": username, "type": "string"})
        params.update({"m": mode, "limit": limit})
        r = requests.get(self.base_url + '/api/get_user_recent', params=params)
        try:
            return user.UserRecent(r.json()[0])
        except IndexError:
            return None
