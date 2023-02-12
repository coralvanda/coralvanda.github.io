"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

import abc
from app import repositories
from app.app import database


class BaseUnitOfWork(abc.ABC):
    pokemon: repositories.BaseRepository

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


class PokeUnitOfWork(BaseUnitOfWork):
    def __enter__(self):
        self.pokemon = repositories.PokemonRepository(df=database)
        return super().__enter__()

    def __exit__(self, *args):
        return super().__exit__(*args)
