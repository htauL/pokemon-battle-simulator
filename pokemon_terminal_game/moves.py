from move import Move
from element_types import Type

MOVES = {
    "Tackle": Move("Tackle", Type.NORMAL, 40, False),
    "Scratch": Move("Scratch", Type.NORMAL, 40, False),
    "Water Gun": Move("Water Gun", Type.WATER, 40, True),
    "Ember": Move("Ember", Type.FIRE, 40, True),
    "Vine Whip": Move("Vine Whip", Type.GRASS, 45, False),
    "Thunder Shock": Move("Thunder Shock", Type.ELECTRIC, 40, True),
    "Quick Attack": Move("Quick Attack", Type.NORMAL, 40, False),
    "Rock Throw": Move("Rock Throw", Type.ROCK, 40, False),
    "Leech Life": Move("Leech Life", Type.BUG, 40, False),
    "Bite": Move("Bite", Type.DARK, 40, False),
    "Fairy Wind": Move("Fairy Wind", Type.FAIRY, 40, True),
    "Pound": Move("Pound", Type.NORMAL, 40, False),
    "Confusion": Move("Confusion", Type.PSYCHIC, 50, True),
    "Lick": Move("Lick", Type.GHOST, 30, False),
    "Peck": Move("Peck", Type.FLYING, 35, False),
    "Poison Sting": Move("Poison Sting", Type.POISON, 15, False),
}
