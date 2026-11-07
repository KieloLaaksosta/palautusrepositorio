import unittest

from src.player_stats import PlayerStats


class StubPlayer:
    def __init__(self, team, score):
        self.team = team
        self._score = score

    def get_score(self):
        return self._score


class TestTopScorersByTeam(unittest.TestCase):
    def test_returns_players_from_team_in_descending_score_order(self):
        player1 = StubPlayer("NYR", 20)
        player2 = StubPlayer("BOS", 35)
        player3 = StubPlayer("NYR", 42)
        player4 = StubPlayer("NYR", 31)
        stats = PlayerStats([player1, player2, player3, player4])

        result = stats.top_scorers_by_team("NYR")

        self.assertEqual(result, [player3, player4, player1])

    def test_returns_empty_list_when_team_has_no_players(self):
        stats = PlayerStats([StubPlayer("NYR", 20)])

        self.assertEqual(stats.top_scorers_by_team("BOS"), [])


if __name__ == "__main__":
    unittest.main()
