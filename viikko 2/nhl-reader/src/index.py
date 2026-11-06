from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    season = input("Season [2018-19 / 2019-20 / 2021-22 / 2022-23 / 2023-24 / 2024-25 / 2025-26] (2024-25): ")
    season = season.strip()
    if season not in ["2018-19", "2019-20", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]:
        season = "2024-25"
        
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader.get_players())
        
    while(True):
        nationality = input("Nationality [USA / FIN / CAN / SWE / CZE / RUS / SLO / FRA / GBR / SVK / DEN / NED / AUT / BLR / GER / SUI / NOR / UZB / LAT / AUS / ALL] (ALL): ")
        nationality = nationality.strip()
        if nationality not in ["USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR", "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS"]:
            nationality = "ALL"

        if nationality != "ALL":
            players = stats.top_scorers_by_nationality(nationality)
        else:
            players = stats.top_scorers()

        print("Players from {nationality}")
        for p in players:
            print(p)
        

if __name__ == "__main__":
    main()