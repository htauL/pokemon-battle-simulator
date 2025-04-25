from battle import start_battle
from pokemons import get_sample_team

if __name__ == "__main__":
    team1 = get_sample_team()
    team2 = get_sample_team()
    start_battle(team1, team2)