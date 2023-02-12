"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

from app import pokemon_app
from app.routes import get_one, get_all


if __name__ == '__main__':
    pokemon_app.run(debug=True)
