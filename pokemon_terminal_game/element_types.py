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
    Type.FLYING: {
        "weaknesses": [Type.ROCK, Type.ELECTRIC, Type.ICE],
        "resistances": [Type.BUG, Type.FIGHTING, Type.GRASS],
        "immunities": [Type.GROUND]
    },
    Type.NORMAL: {
        "weaknesses": [Type.FIGHTING],
        "resistances": [],
        "immunities": [Type.GHOST]
    },
    Type.FIRE: {
        "weaknesses": [Type.WATER, Type.ROCK],
        "resistances": [Type.BUG, Type.FIRE, Type.GRASS],
        "immunities": []
    },
    Type.WATER: {
        "weaknesses": [Type.ELECTRIC, Type.GRASS],
        "resistances": [Type.FIRE, Type.WATER],
        "immunities": []
    },
    Type.GRASS: {
        "weaknesses": [Type.FIRE, Type.BUG],
        "resistances": [Type.WATER, Type.GRASS],
        "immunities": []
    },
    Type.ELECTRIC: {
        "weaknesses": [Type.GROUND],
        "resistances": [Type.ELECTRIC],
        "immunities": []
    },
    Type.ROCK: {
        "weaknesses": [Type.WATER, Type.GRASS, Type.FIGHTING],
        "resistances": [Type.NORMAL, Type.FIRE],
        "immunities": []
    },
    Type.BUG: {
        "weaknesses": [Type.FIRE, Type.ROCK],
        "resistances": [Type.GRASS, Type.FIGHTING],
        "immunities": []
    },
    Type.DARK: {
        "weaknesses": [Type.FIGHTING, Type.BUG],
        "resistances": [Type.DARK],
        "immunities": [Type.PSYCHIC]
    },
    Type.GROUND: {
        "weaknesses": [Type.WATER, Type.GRASS],
        "resistances": [Type.ROCK],
        "immunities": [Type.ELECTRIC]
    },
    Type.FIGHTING: {
        "weaknesses": [Type.FLYING],
        "resistances": [Type.BUG, Type.ROCK],
        "immunities": []
    },
    Type.ICE: {
        "weaknesses": [Type.FIRE, Type.ROCK],
        "resistances": [],
        "immunities": []
    },
    Type.GHOST: {
        "weaknesses": [Type.DARK],
        "resistances": [],
        "immunities": [Type.NORMAL, Type.FIGHTING]
    },
    Type.PSYCHIC: {
        "weaknesses": [Type.DARK, Type.BUG],
        "resistances": [],
        "immunities": []
    }
}
