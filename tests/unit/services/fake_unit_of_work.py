"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

from app.entities.pokemon import Pokemon
from app.services.unit_of_work import BaseUnitOfWork
from app.repositories.base_repository import BaseRepository


class BasePokeRepo(BaseRepository):
    pokemon = [
        Pokemon(**{
            "pokedex_number": 1,
            "attack": 49,
            "defense": 49,
            "generation": 1,
            "hp": 45,
            "legendary": False,
            "name": "Bulbasaur",
            "sp_atk": 65,
            "sp_def": 65,
            "speed": 45,
            "total": 318,
            "type_1": "Grass",
            "type_2": "Poison"
        }),
        Pokemon(**{
            "pokedex_number": 4,
            "attack": 52,
            "defense": 43,
            "generation": 1,
            "hp": 39,
            "legendary": False,
            "name": "Charmander",
            "sp_atk": 60,
            "sp_def": 50,
            "speed": 65,
            "total": 309,
            "type_1": "Fire",
            "type_2": ""
        }),
        Pokemon(**{
            "pokedex_number": 7,
            "attack": 48,
            "defense": 65,
            "generation": 1,
            "hp": 44,
            "legendary": False,
            "name": "Squirtle",
            "sp_atk": 50,
            "sp_def": 64,
            "speed": 43,
            "total": 314,
            "type_1": "Water",
            "type_2": ""
        })
    ]

    def get_one(self, poke_id):
        target_pokemon = [p for p in self.pokemon if p.pokedex_number == poke_id]
        return target_pokemon[0] if target_pokemon else None

    def get_all(self):
        return self.pokemon


class FakeUnitOfWork(BaseUnitOfWork):
    def __init__(self):
        self.pokemon = BasePokeRepo()
