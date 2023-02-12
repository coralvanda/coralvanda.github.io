"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

from flask import Flask
from app.orm import initialize_database

pokemon_app = Flask(__name__)
database = initialize_database()


if __name__ == '__main__':
    pokemon_app.run()
