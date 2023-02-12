"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""
from flask import Flask
from orm import initialize_database

pokemon_app = Flask(__name__)
database = initialize_database()
