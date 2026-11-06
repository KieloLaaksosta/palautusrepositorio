from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.table import Table

valid_seasons = ["2018-19", "2019-20", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]
default_season = "2024-25"

valid_nationalities = [
    "USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA",
    "GBR", "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI",
    "NOR", "UZB", "LAT", "AUS"
]
default_nationality = "ALL"

def main():
    print(f"Season [magenta][{" / ".join(valid_seasons)}][/magenta] [cyan]({default_season})[/cyan]: ")
    season_input = input()
    season = season_input.strip()

    if season not in valid_seasons:
        season = default_season

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader.get_players())

    while True:
        print(f"\nNationality [magenta][{" / ".join(valid_nationalities)}][/magenta] [cyan]({default_nationality})[/cyan]: ")
        nat_input = input()
        nationality = nat_input.strip().upper()

        if nationality not in valid_nationalities:
            nationality = default_nationality

        if nationality != "ALL":
            players = stats.top_scorers_by_nationality(nationality)
        else:
            players = stats.top_scorers()

        print(f"\n[bold] Season {season} players from {nationality} [/bold]")

        table = Table(show_header=True, header_style="bold")
        table.add_column("Name", style="cyan", width=22)
        table.add_column("Team", style="magenta", width=8)
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="bold green")

        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.get_score())
            )

        print(table)

if __name__ == "__main__":
    main()