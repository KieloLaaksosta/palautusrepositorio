import unittest
from statistics_service import StatisticsService, PlayerReader

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.service = StatisticsService(
            PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt")
        )

    def test_search_valid_name(self):
        player = self.service.search("Owen Tippett")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Owen Tippett")
        self.assertEqual(player.team, "PHI")
        
    def test_search_invalid_name(self):
        player = self.service.search("Matti Meikäläinen")
        self.assertIsNone(player)
        
    def test_search_team(self):
        players = self.service.team("PHI")
        self.assertGreater(len(players), 0)
        for player in players:
            self.assertEqual(player.team, "PHI")
    
    def test_top(self):
        top_players = self.service.top(2)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Nikita Kucherov")
        self.assertEqual(top_players[1].name, "Nathan MacKinnon")
        self.assertEqual(top_players[2].name, "David Pastrnak")