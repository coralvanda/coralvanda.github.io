"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

from flask import abort

from typing import List
from app.services.unit_of_work import BaseUnitOfWork


def get_single_pokemon(pokedex_number: int, unit_of_work: BaseUnitOfWork) -> dict:
    """
    Finds and returns a single pokemon based on the index number

    Parameters
    ----------
    pokedex_number: int
    unit_of_work: BaseUnitOfWork

    Returns
    -------
    dict
    """
    with unit_of_work:
        target_pokemon = unit_of_work.pokemon.get_one(poke_id=pokedex_number)

    if target_pokemon is None:
        abort(404)

    return target_pokemon.to_dict()


def get_all_pokemon(unit_of_work: BaseUnitOfWork) -> List[dict]:
    """
    Returns all pokemon in the database

    Parameters
    ----------
    unit_of_work: BaseUnitOfWork

    Returns
    -------
    List[dict]
    """
    with unit_of_work:
        all_pokemon = unit_of_work.pokemon.get_all()

    return [pokemon.to_dict() for pokemon in all_pokemon]
