"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

import os

from flask import make_response, Response
from openapi_core import Spec
from openapi_core.contrib.flask.decorators import FlaskOpenAPIViewDecorator

from app import pokemon_app
from app.services import poke_services, PokeUnitOfWork


spec = Spec.from_file_path(os.path.join(
    os.path.abspath(__file__),
    os.pardir,
    os.pardir,
    os.pardir,
    'openapi.yaml')
)
openapi_validator = FlaskOpenAPIViewDecorator.from_spec(spec)


@pokemon_app.route('/pokemon')
@openapi_validator
def get_all():
    """
    Endpoint to list all pokemon

    Returns
    -------
    Response
    """
    pokemon_list = poke_services.get_all_pokemon(unit_of_work=PokeUnitOfWork())
    return make_response(pokemon_list, 200)


@pokemon_app.route('/pokemon/<int:id>')
@openapi_validator
def get_one(id: int):
    """
    Endpoint to retrieve a single pokemon by ID

    Parameters
    ----------
    id: int

    Returns
    -------
    Response
    """
    target_pokemon = poke_services.get_single_pokemon(
        pokedex_number=id,
        unit_of_work=PokeUnitOfWork()
    )
    return make_response(target_pokemon, 200)
