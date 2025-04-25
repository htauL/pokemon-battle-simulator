import time
from element_types import type_chart

# Tokyo Night-inspired ANSI color codes
RESET   = "\033[0m"
CYAN    = "\033[96m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
YELLOW  = "\033[93m"
GREEN   = "\033[92m"
RED     = "\033[91m"
BOLD    = "\033[1m"

# Colored name helper based on Pokemon primary type
def get_colored_name(pokemon):
    color = MAGENTA  # default for other types
    if pokemon.type1 == "WATER":
        color = BLUE
    elif pokemon.type1 == "FIRE":
        color = YELLOW
    elif pokemon.type1 == "GRASS":
        color = GREEN
    return f"{color}{pokemon.name}{RESET}"

# Colored move name based on type (customize if desired)
def get_colored_move(move):
    color = MAGENTA
    if move.type == "WATER":
        color = BLUE
    elif move.type == "FIRE":
        color = YELLOW
    elif move.type == "GRASS":
        color = GREEN
    return f"{color}{move.name}{RESET}"

# Utility function to print messages with delay
def delay_print(message, delay=0.75):
    print(message)
    time.sleep(delay)

# Start a battle between two teams of Pokemon
def start_battle(player_team, opponent_team):
    delay_print(f"{BOLD}A battle begins!{RESET}")
    delay_print("Team 1: " + ", ".join([get_colored_name(p) for p in player_team]))
    print("Team 2: " + ", ".join([get_colored_name(p) for p in opponent_team]))

    player_index = choose_pokemon(player_team)
    opponent_index = 0

    while player_index < len(player_team) and opponent_index < len(opponent_team):
        player_pokemon = player_team[player_index]
        opponent_pokemon = opponent_team[opponent_index]

        delay_print(f"\n⚔️ {get_colored_name(player_pokemon)} enters the battle against {get_colored_name(opponent_pokemon)}!")

        while not player_pokemon.fainted and not opponent_pokemon.fainted:
            delay_print(f"\n{get_colored_name(player_pokemon)} HP: {player_pokemon.current_hp}/{player_pokemon.max_hp}")
            print(f"{get_colored_name(opponent_pokemon)} HP: {opponent_pokemon.current_hp}/{opponent_pokemon.max_hp}")

            delay_print(f"\n{BOLD}Choose a move:{RESET}")
            for index, move in enumerate(player_pokemon.moves):
                print(f"{index + 1}. {get_colored_move(move)}")

            try:
                selected_index = int(input("Enter move number: ")) - 1
                selected_move = player_pokemon.moves[selected_index]

                # Player attacks
                damage, multiplier = calculate_damage(player_pokemon, opponent_pokemon, selected_move)
                opponent_pokemon.take_damage(damage)
                delay_print(f"{get_colored_name(player_pokemon)} used {get_colored_move(selected_move)} and dealt {BOLD}{damage}{RESET} damage!")

                # Show effectiveness
                if multiplier == 0:
                    delay_print(f"{RED}It doesn't affect {get_colored_name(opponent_pokemon)}...{RESET}")
                elif multiplier >= 2:
                    delay_print(f"{YELLOW}It's super effective!{RESET}")
                elif multiplier < 1:
                    delay_print(f"{CYAN}It's not very effective...{RESET}")

                if opponent_pokemon.fainted:
                    delay_print(f"{get_colored_name(opponent_pokemon)} fainted!")
                    opponent_index += 1
                    if opponent_index >= len(opponent_team):
                        delay_print(f"\n{BOLD}{GREEN}🎉 You defeated all opponent Pokemon. Victory!{RESET}")
                        return
                    break

                # Opponent attacks (AI logic - first move)
                enemy_move = opponent_pokemon.moves[0]
                damage, multiplier = calculate_damage(opponent_pokemon, player_pokemon, enemy_move)
                player_pokemon.take_damage(damage)
                delay_print(f"{get_colored_name(opponent_pokemon)} used {get_colored_move(enemy_move)} and dealt {BOLD}{damage}{RESET} damage!")

                if multiplier == 0:
                    delay_print(f"{RED}It doesn't affect {get_colored_name(player_pokemon)}...{RESET}")
                elif multiplier >= 2:
                    delay_print(f"{YELLOW}It's super effective!{RESET}")
                elif multiplier < 1:
                    delay_print(f"{CYAN}It's not very effective...{RESET}")

                if player_pokemon.fainted:
                    delay_print(f"{get_colored_name(player_pokemon)} fainted!")
                    if (check_for_unfainted_pokemon(player_team)):
                        player_index = choose_pokemon(player_team)
                    else:
                        delay_print(f"\n{BOLD}{RED}💀 All your Pokemon fainted. You lost the battle!{RESET}")
                        return
                    break

            except ValueError:
                delay_print(f"{RED}Invalid input! Please enter a valid move number.{RESET}")
            except IndexError:
                delay_print(f"{RED}Invalid move selection! Please choose a valid move number.{RESET}")

    if player_index >= len(player_team):
        delay_print(f"\n{BOLD}{RED}💀 All your Pokemon fainted. You lost the battle!{RESET}")
    elif opponent_index >= len(opponent_team):
        delay_print(f"\n{BOLD}{GREEN}🎉 You defeated all opponent Pokemon. Victory!{RESET}")

# Calculate damage between two Pokemon given a move
def calculate_damage(attacker, defender, move):
    if move.is_special:
        attack_stat = attacker.sp_atk
        defense_stat = defender.sp_def
    else:
        attack_stat = attacker.atk
        defense_stat = defender.defense

    defender_types = [defender.type1]
    if defender.type2:
        defender_types.append(defender.type2)

    type_multiplier = get_type_effectiveness(move.type, defender_types)

    base_damage = ((2 * 50 / 5 + 2) * move.power * attack_stat / defense_stat) / 50 + 2
    total_damage = base_damage * type_multiplier

    return (0 if type_multiplier == 0 else max(1, int(total_damage))), type_multiplier

# Determine how effective a move's type is against the defender's types
def get_type_effectiveness(move_type, defender_types):
    multiplier = 1.0
    for d_type in defender_types:
        chart = type_chart.get(d_type, {})
        if move_type in chart.get("immunities", []):
            return 0.0
        elif move_type in chart.get("weaknesses", []):
            multiplier *= 2.0
        elif move_type in chart.get("resistances", []):
            multiplier *= 0.5
    return multiplier

def choose_pokemon(team):
    while True:
        delay_print(f"\n{BOLD}Choose a pokemon:{RESET}")
        for index, pokemon in enumerate(team):
            fainted_text = ""
            if (pokemon.fainted):
                fainted_text = "(fainted)"
            print(f"{index + 1}. {get_colored_name(pokemon)}{RESET}{fainted_text}")
        
        try:
            selected_index = int(input("Enter pokemon number: ")) - 1

            # Out of bounds check
            if selected_index < 0 or selected_index >= len(team):
                raise IndexError
            
            # Check if the Pokemon is fainted
            if team[selected_index].fainted:
                raise FaintedPokemonSelected("You can't choose a fainted Pokemon!")

            delay_print(f"\n{BOLD}Go, {get_colored_name(team[selected_index])}!")

            return selected_index
        
        except ValueError:
            delay_print(f"{RED}Invalid input! Please enter a valid pokemon number.{RESET}")
        except IndexError:
            delay_print(f"{RED}Invalid pokemon selection! Please choose a valid pokemon number.{RESET}")
        except FaintedPokemonSelected as e:
            delay_print(f"{RED}{e}{RESET}")

def check_for_unfainted_pokemon(team):
    return any(not pokemon.fainted for pokemon in team)

class FaintedPokemonSelected(Exception):
    pass


    
