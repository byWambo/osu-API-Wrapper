class Match:

    def __init__(self, data):
        self.match_id = data['match_id']
        self.name = data['name']
        self.start_time = data['start_time']
        self.end_time = data['end_time']