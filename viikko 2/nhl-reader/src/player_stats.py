from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, players):

        self._players = players

    def top_scorers_by_nationality(self, nationality):
        filtered_players = [p for p in self._players if p.nationality == nationality]
        filtered_players.sort(key= lambda p: -p.get_score())
        
        return filtered_players
