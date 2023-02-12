"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

from app import pokemon_app
from app.services import poke_services, PokeUnitOfWork


@pokemon_app.route('/pokemon')
def get_all():
    pokemon_list = poke_services.get_all_pokemon(unit_of_work=PokeUnitOfWork())
    return pokemon_list


@pokemon_app.route('/pokemon/<int:id>')
def get_one(id):
    target_pokemon = poke_services.get_single_pokemon(
        pokedex_number=id,
        unit_of_work=PokeUnitOfWork()
    )
    return target_pokemon
