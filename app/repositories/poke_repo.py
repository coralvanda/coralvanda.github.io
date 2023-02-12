"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

from app.entities import build_pokemon_from_series
from app.repositories.base_repository import BaseRepository


class PokemonRepository(BaseRepository):
    def __init__(self, df):
        super().__init__()
        self.df = df

    def get_one(self, poke_id):
        selected_pokemon = self.df[self.df['#'].eq(poke_id)]
        return build_pokemon_from_series(series=selected_pokemon)

    def get_all(self):
        all_pokemon = self.df.apply(lambda x: build_pokemon_from_series(x), axis=1)
        return all_pokemon
