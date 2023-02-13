"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

import pandas


def initialize_database() -> pandas.DataFrame:
    """
    Creates a pandas dataframe of the pokemon data for use as a simple in-memory database

    Returns
    -------
    pandas.DataFrame
    """
    df = pandas.read_json('https://coralvanda.github.io/pokemon_data.json')

    return df
