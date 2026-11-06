from dataclasses import dataclass
import requests

def get_players(url):
    try:
        response = requests.get(url, timeout=10).json()
    except requests.exceptions.Timeout:
        return None
    return [create_player(p) for p in response]

def create_player(player_dict):
    return Player(
        player_dict["name"],
        player_dict["team"],
        player_dict["nationality"],
        player_dict["goals"],
        player_dict["assists"]
    )

@dataclass
class Player:
    name: str
    team: str
    nationality: str
    goals: int
    assists: int

    def get_score(self):
        return self.assists + self.goals
