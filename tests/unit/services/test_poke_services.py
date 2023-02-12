"""
Principal Author: Eric Linden
Description :

Notes :
February 12, 2023
"""

import pytest
from werkzeug.exceptions import HTTPException

from app.services import poke_services
from tests.unit.services.fake_unit_of_work import FakeUnitOfWork


def test_get_single_pokemon_should_return_correct_value():
    response = poke_services.get_single_pokemon(1, FakeUnitOfWork())

    assert response.get('Name') == 'Bulbasaur'


def test_get_single_pokemon_should_abort_if_no_result():
    with pytest.raises(HTTPException) as e:
        poke_services.get_single_pokemon(999, FakeUnitOfWork())

        assert e.value.args[0] == 404


def test_get_all_pokemon_should_return_full_list():
    response = poke_services.get_all_pokemon(FakeUnitOfWork())

    assert len(response) == 3
