import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN:")

    finnish_players = [p for p in players if p.nationality == "FIN"]
    for p in finnish_players:
        print(p)
        

if __name__ == "__main__":
    main()