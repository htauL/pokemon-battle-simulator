from enum import Enum

class Type(Enum):
    NORMAL = "Normal"
    FIRE = "Fire"
    WATER = "Water"
    GRASS = "Grass"
    ELECTRIC = "Electric"
    ICE = "Ice"
    FIGHTING = "Fighting"
    POISON = "Poison"
    GROUND = "Ground"
    FLYING = "Flying"
    PSYCHIC = "Psychic"
    BUG = "Bug"
    ROCK = "Rock"
    GHOST = "Ghost"
    DRAGON = "Dragon"
    DARK = "Dark"
    STEEL = "Steel"
    FAIRY = "Fairy"

# Type chart with weaknesses, resistances, and immunities
type_chart = {
    Type.NORMAL: {
        "weaknesses": [Type.FIGHTING],
        "resistances": [],
        "immunities": [Type.GHOST]
    },
    Type.FIRE: {
        "weaknesses": [Type.WATER, Type.GROUND, Type.ROCK],
        "resistances": [Type.BUG, Type.STEEL, Type.FIRE, Type.GRASS, Type.ICE, Type.FAIRY],
        "immunities": []
    },
    Type.WATER: {
        "weaknesses": [Type.ELECTRIC, Type.GRASS],
        "resistances": [Type.STEEL, Type.FIRE, Type.WATER, Type.ICE],
        "immunities": []
    },
    Type.ELECTRIC: {
        "weaknesses": [Type.GROUND],
        "resistances": [Type.FLYING, Type.STEEL, Type.ELECTRIC],
        "immunities": []
    },
    Type.GRASS: {
        "weaknesses": [Type.FIRE, Type.ICE, Type.POISON, Type.FLYING, Type.BUG],
        "resistances": [Type.GROUND, Type.WATER, Type.GRASS, Type.ELECTRIC],
        "immunities": []
    },
    Type.ICE: {
        "weaknesses": [Type.FIRE, Type.FIGHTING, Type.ROCK, Type.STEEL],
        "resistances": [Type.ICE],
        "immunities": []
    },
    Type.FIGHTING: {
        "weaknesses": [Type.FLYING, Type.PSYCHIC, Type.FAIRY],
        "resistances": [Type.ROCK, Type.BUG, Type.DARK],
        "immunities": []
    },
    Type.POISON: {
        "weaknesses": [Type.GROUND, Type.PSYCHIC],
        "resistances": [Type.FIGHTING, Type.POISON, Type.BUG, Type.GRASS, Type.FAIRY],
        "immunities": []
    },
    Type.GROUND: {
        "weaknesses": [Type.WATER, Type.GRASS, Type.ICE],
        "resistances": [Type.POISON, Type.ROCK],
        "immunities": [Type.ELECTRIC]
    },
    Type.FLYING: {
        "weaknesses": [Type.ROCK, Type.ELECTRIC, Type.ICE],
        "resistances": [Type.FIGHTING, Type.BUG, Type.GRASS],
        "immunities": [Type.GROUND]
    },
    Type.PSYCHIC: {
        "weaknesses": [Type.BUG, Type.GHOST, Type.DARK],
        "resistances": [Type.FIGHTING, Type.PSYCHIC],
        "immunities": []
    },
    Type.BUG: {
        "weaknesses": [Type.FLYING, Type.ROCK, Type.FIRE],
        "resistances": [Type.FIGHTING, Type.GRASS, Type.GROUND],
        "immunities": []
    },
    Type.ROCK: {
        "weaknesses": [Type.FIGHTING, Type.GROUND, Type.STEEL, Type.WATER, Type.GRASS],
        "resistances": [Type.NORMAL, Type.FIRE, Type.POISON, Type.FLYING],
        "immunities": []
    },
    Type.GHOST: {
        "weaknesses": [Type.GHOST, Type.DARK],
        "resistances": [Type.POISON, Type.BUG],
        "immunities": [Type.NORMAL, Type.FIGHTING]
    },
    Type.DRAGON: {
        "weaknesses": [Type.ICE, Type.DRAGON, Type.FAIRY],
        "resistances": [Type.FIRE, Type.WATER, Type.ELECTRIC, Type.GRASS],
        "immunities": []
    },
    Type.DARK: {
        "weaknesses": [Type.FIGHTING, Type.BUG, Type.FAIRY],
        "resistances": [Type.GHOST, Type.DARK],
        "immunities": [Type.PSYCHIC]
    },
    Type.STEEL: {
        "weaknesses": [Type.FIGHTING, Type.GROUND, Type.FIRE],
        "resistances": [Type.NORMAL, Type.GRASS, Type.ICE, Type.FLYING, Type.PSYCHIC, Type.BUG, Type.ROCK, Type.DRAGON, Type.STEEL, Type.FAIRY],
        "immunities": [Type.POISON]
    },
    Type.FAIRY: {
        "weaknesses": [Type.POISON, Type.STEEL],
        "resistances": [Type.FIGHTING, Type.BUG, Type.DARK],
        "immunities": [Type.DRAGON]
    }
}
