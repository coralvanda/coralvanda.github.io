"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

import abc
from app.repositories import BaseRepository, PokemonRepository
from app import database


class BaseUnitOfWork(abc.ABC):
    pokemon: BaseRepository

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


class PokeUnitOfWork(BaseUnitOfWork):
    def __enter__(self):
        self.pokemon = PokemonRepository(df=database)
        return super().__enter__()

    def __exit__(self, *args):
        return super().__exit__(*args)
