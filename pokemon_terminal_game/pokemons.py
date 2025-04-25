import random
from pokemon import Pokemon
from element_types import Type
from moves import MOVES

# Pokemon definitions
POKEMON_DATABASE = [
    Pokemon("Squirtle", Type.WATER, None, 44, 48, 50, 64, 60, 43, [MOVES["Water Gun"], MOVES["Tackle"]]),
    Pokemon("Charmander", Type.FIRE, None, 39, 52, 43, 50, 58, 65, [MOVES["Ember"], MOVES["Scratch"]]),
    Pokemon("Bulbasaur", Type.GRASS, Type.POISON, 45, 49, 49, 65, 59, 45, [MOVES["Vine Whip"], MOVES["Tackle"]]),
    Pokemon("Pikachu", Type.ELECTRIC, None, 35, 55, 40, 50, 50, 90, [MOVES["Thunder Shock"], MOVES["Quick Attack"]]),
    Pokemon("Geodude", Type.ROCK, Type.GROUND, 40, 80, 100, 30, 40, 20, [MOVES["Tackle"], MOVES["Rock Throw"]]),
    Pokemon("Zubat", Type.POISON, Type.FLYING, 40, 45, 35, 40, 40, 55, [MOVES["Leech Life"], MOVES["Quick Attack"]]),
    Pokemon("Psyduck", Type.WATER, None, 50, 52, 48, 50, 60, 55, [MOVES["Water Gun"], MOVES["Scratch"]]),
    Pokemon("Growlithe", Type.FIRE, None, 55, 70, 45, 50, 45, 60, [MOVES["Ember"], MOVES["Bite"]]),
    Pokemon("Poliwag", Type.WATER, None, 40, 50, 40, 40, 40, 90, [MOVES["Water Gun"], MOVES["Tackle"]]),
    Pokemon("Machop", Type.FIGHTING, None, 70, 80, 50, 35, 35, 35, [MOVES["Tackle"], MOVES["Rock Throw"]]),
    Pokemon("Bellsprout", Type.GRASS, Type.POISON, 50, 75, 35, 70, 30, 40, [MOVES["Vine Whip"], MOVES["Poison Sting"]]),
    Pokemon("Magnemite", Type.ELECTRIC, Type.STEEL, 25, 35, 70, 95, 55, 45, [MOVES["Thunder Shock"], MOVES["Tackle"]]),
    Pokemon("Gastly", Type.GHOST, Type.POISON, 30, 35, 30, 100, 35, 80, [MOVES["Lick"], MOVES["Confusion"]]),
    Pokemon("Clefairy", Type.FAIRY, None, 70, 45, 48, 60, 65, 35, [MOVES["Fairy Wind"], MOVES["Pound"]]),
    Pokemon("Jigglypuff", Type.NORMAL, Type.FAIRY, 115, 45, 20, 45, 25, 20, [MOVES["Pound"], MOVES["Fairy Wind"]]),
    Pokemon("Abra", Type.PSYCHIC, None, 25, 20, 15, 105, 55, 90, [MOVES["Confusion"]]),
    Pokemon("Oddish", Type.GRASS, Type.POISON, 45, 50, 55, 75, 65, 30, [MOVES["Vine Whip"], MOVES["Poison Sting"]]),
    Pokemon("Vulpix", Type.FIRE, None, 38, 41, 40, 50, 65, 65, [MOVES["Ember"], MOVES["Quick Attack"]]),
    Pokemon("Meowth", Type.NORMAL, None, 40, 45, 35, 40, 40, 90, [MOVES["Scratch"], MOVES["Bite"]]),
    Pokemon("Ekans", Type.POISON, None, 35, 60, 44, 40, 54, 55, [MOVES["Poison Sting"], MOVES["Bite"]]),
    Pokemon("Pidgey", Type.NORMAL, Type.FLYING, 40, 45, 40, 35, 35, 56, [MOVES["Tackle"], MOVES["Peck"]]),
    Pokemon("Rattata", Type.NORMAL, None, 30, 56, 35, 25, 35, 72, [MOVES["Quick Attack"], MOVES["Bite"]]),
]


def get_sample_team():
    # Return 3 random Pokemon without duplicates
    return random.sample(POKEMON_DATABASE, 3)
