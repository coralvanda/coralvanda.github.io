"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

import pandas


def initialize_database():
    df = pandas.read_json('https://coralvanda.github.io/pokemon_data.json')

    return df
