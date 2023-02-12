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
        dict_form = dataclasses.asdict(self)
        pokedex_number = dict_form.pop('pokedex_number')
        dict_form = {
            '#': pokedex_number,
            **dict_form
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
