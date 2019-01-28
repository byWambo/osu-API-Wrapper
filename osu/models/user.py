__slots__ = ('User', 'UserRecent', 'UserBest')


class User:

    def __init__(self, data):
        self.id = data['user_id']
        self.name = data['username']
        self.join_date = data['join_date']
        self.three_hundred = data['count300']
        self.hundred = data['count100']
        self.fifty = data['count50']
        self.play = data['playcount']
        self.ranked_score = data['ranked_score']
        self.total_score = data['total_score']
        self.pp = data['pp_rank']
        self.level = data['level']
        self.pp_raw = data['pp_raw']
        self.accuracy = data['accuracy']
        self.ss = data['count_rank_ss']
        self.ss_plus = data['count_rank_ssh']
        self.s = data['count_rank_s']
        self.s_plus = data['count_rank_sh']
        self.a = data['count_rank_a']
        self.country = data['country']
        self.total_seconds_played = data['total_seconds_played']
        self.country_rank = data['pp_country_rank']

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<osu.User id={0.id} name={0.name}>'.format(self)


class UserRecent:

    def __init__(self, data):
        self.beatmap = NotImplemented
        self.score = data["score"]
        self.maxcombo = data["maxcombo"]
        self.three_hundred = data["count300"]
        self.hundred = data["count100"]
        self.fifty = data["count50"]
        self.misses = data["countmiss"]
        self.katu = data["countkatu"]
        self.geki = data["countgeki"]
        self.perfect = data["perfect"]
        self.mods = NotImplemented
        self.user_id = data["user_id"]
        self.date = data["data"]
        self.rank = data["rank"]

    def __repr__(self):
        return '<osu.RecentlyPlayed user_id={0.user_id}>'.format(self)


class UserBest:

    def __init__(self, data):
        self.beatmap = NotImplemented
        self.score = data["score"]
        self.maxcombo = data["maxcombo"]
        self.three_hundred = data["count300"]
        self.hundred = data["count100"]
        self.fifty = data["count50"]
        self.misses = data["countmiss"]
        self.katu = data["countkatu"]
        self.geki = data["countgeki"]
        self.perfect = data["perfect"]
        self.mods = NotImplemented
        self.user_id = data["user_id"]
        self.date = data["data"]
        self.rank = data["rank"]
        self.pp = data['pp']

    def __repr__(self):
        return '<osu.BestPerformance user_id={0.user_id} pp={0.pp}>'.format(self)
