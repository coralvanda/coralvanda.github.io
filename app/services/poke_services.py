"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

from typing import List
from app.services import BaseUnitOfWork


def get_single_pokemon(pokedex_number: int, unit_of_work: BaseUnitOfWork) -> str:
    with unit_of_work:
        target_pokemon = unit_of_work.pokemon.get_one(poke_id=pokedex_number)

    return target_pokemon.as_json()


def get_all_pokemon(unit_of_work: BaseUnitOfWork) -> List[str]:
    with unit_of_work:
        all_pokemon = unit_of_work.pokemon.get_all()

    return [pokemon.as_json() for pokemon in all_pokemon]
