from . import game, match


class MultiplayerMatch:

    def __init__(self, data):
        self.match = match.Match(data['match'])
        self.games = [game for game in game.Game(data['match'])]