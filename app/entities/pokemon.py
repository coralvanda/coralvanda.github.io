"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

import dataclasses
import json


@dataclasses.dataclass
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

    def to_dict(self):
        dict_form = {
            '#': int(self.pokedex_number),
            'Name': self.name,
            'Type 1': self.type_1,
            'Type 2': self.type_2 if self.type_2 is not None else '',
            'Total': int(self.total),
            'HP': int(self.hp),
            'Attack': int(self.attack),
            'Defense': int(self.defense),
            'Sp. Atk': int(self.sp_atk),
            'Sp. Def': int(self.sp_def),
            'Speed': int(self.speed),
            'Generation': int(self.generation),
            'Legendary': bool(self.legendary)
        }
        return dict_form

    def to_json(self):
        dict_form = self.to_dict()
        return json.dumps(dict_form)


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
