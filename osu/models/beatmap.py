__slots__ = ('Beatmap', 'Scores')


class Beatmap:

    def __init__(self, data):
        self.approved = data['approved']
        self.approved_date = data['approved_date']
        self.last_update = data['last_update']
        self.artist = data['artist']
        self.beatmap_id = data['beatmap_id']
        self.beatmapset_id = data['beatmapset_id']
        self.bpm = data['bpm']
        self.creator = data['creator']
        self.creator_id = data['creator_id']
        self.difficulty = data['difficultyrating']
        self.circle_size = data['diff_size']
        self.overall_difficulty = data['diff_overall']
        self.approach_rate = data['diff_approach']
        self.hp_drain = data['diff_drain']
        self.hit_length = data['hit_length']
        self.source = data['source']
        self.genre_id = data['genre_id']
        self.language_id = data['language_id']
        self.title = data['title']
        self.total_length = data['total_length']
        self.version = data['version']
        self.file_md5 = data['file_md5']
        self.mode = data['mode']
        self.tags = data['tags']
        self.favourite_count = data['favourite_count']
        self.play_count = data['playcount']
        self.pass_count = data['passcount']
        self.max_combo = data['max_combo']

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<osu.Beatmap title={0.title} creator={0.creator}>'.format(self)


class Scores:

    def __init__(self, data):
        self.score_id = data['score_id']
        self.score = data["score"]
        self.username = data['username']
        self.max_combo = data["maxcombo"]
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
        self.replay_available = data['replay_available']

    def __str__(self):
        return self.username

    def __repr__(self):
        return '<osu.Score user={0.username} pp={0.pp}>'.format(self)
