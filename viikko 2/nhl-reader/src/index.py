from rich import print as rprint
from rich.table import Table
from player import get_players
from player_stats import PlayerStats

VALID_SEASONS = ["2018-19", "2019-20", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]
DEFAULT_SEASON = "2024-25"

VALID_NATIONALITIES = [
    "USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA",
    "GBR", "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI",
    "NOR", "UZB", "LAT", "AUS"
]
DEFAULT_NATIONALITY = "ALL"

def get_season():
    seasons_str = " / ".join(VALID_SEASONS)
    season_options = f"Season [magenta][{seasons_str}][/magenta]"
    season_default = f" [cyan]({DEFAULT_SEASON})[/cyan]: "
    rprint(season_options + season_default)
    season_input = input()
    season = season_input.strip()

    if season not in VALID_SEASONS:
        season = DEFAULT_SEASON

    return season

def get_nationality():
    nationalities_str = " / ".join(VALID_NATIONALITIES)
    nat_options = f"\nNationality [magenta][{nationalities_str}][/magenta]"
    nat_default = f" [cyan]({DEFAULT_NATIONALITY})[/cyan]: "
    rprint(nat_options + nat_default)

    nat_input = input()
    nationality = nat_input.strip().upper()

    if nationality not in VALID_NATIONALITIES:
        nationality = DEFAULT_NATIONALITY

    return nationality

def print_player(players, season, nationality):
    rprint(f"\n[bold] Season {season} players from {nationality} [/bold]")

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

    rprint(table)

def main():
    season = get_season()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(get_players(url))

    while True:
        nationality = get_nationality()

        if nationality != "ALL":
            players = stats.top_scorers_by_nationality(nationality)
        else:
            players = stats.top_scorers()

        print_player(players, season, nationality)

if __name__ == "__main__":
    main()
