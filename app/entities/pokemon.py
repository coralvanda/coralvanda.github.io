"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

from dataclasses import dataclass


@dataclass
class Pokemon:
    pokedex_number: int
    name: str
    type_1: str
    type_2: str
    total: int
    hp: int
    attack: int
    defense: int
    sp_atk: int
    sp_def: int
    speed: int
    generation: int
    legendary: bool


def build_pokemon_from_series(series):
    return Pokemon(
        pokedex_number=series['#'],
        name=series['Name'],
        type_1=series['Type 1'],
        type_2=series['Type 2'],
        total=series['Total'],
        hp=series['HP'],
        attack=series['Attack'],
        defense=series['Defense'],
        sp_atk=series['Sp. Atk'],
        sp_def=series['Sp. Def'],
        speed=series['Speed'],
        generation=series['Generation'],
        legendary=series['Legendary'],
    )
