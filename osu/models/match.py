class Match:

    def __init__(self, data):
        self.id = data['match_id']
        self.name = data['name']
        self.start_time = data['start_time']
        self.end_time = data['end_time']

    def __repr__(self):
        return '<osu.Match match_id={0.id} name={0.name}>'.format(self)