"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

from app.app import pokemon_app


@pokemon_app.route('/')
def get_all():
    raise NotImplementedError


@pokemon_app.route('/<id>')
def get_one(id):
    raise NotImplementedError
