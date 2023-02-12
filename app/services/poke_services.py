"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

from flask import abort

from typing import List
from app.services.unit_of_work import BaseUnitOfWork


def get_single_pokemon(pokedex_number: int, unit_of_work: BaseUnitOfWork) -> str:
    with unit_of_work:
        target_pokemon = unit_of_work.pokemon.get_one(poke_id=pokedex_number)

    if not target_pokemon:
        abort(404)

    return target_pokemon.to_json()


def get_all_pokemon(unit_of_work: BaseUnitOfWork) -> List[str]:
    with unit_of_work:
        all_pokemon = unit_of_work.pokemon.get_all()

    return [pokemon.to_json() for pokemon in all_pokemon]
