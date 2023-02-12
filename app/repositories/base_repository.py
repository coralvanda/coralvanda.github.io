"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

import abc


class BaseRepository(abc.ABC):
    @abc.abstractmethod
    def get_one(self, poke_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all(self):
        raise NotImplementedError
