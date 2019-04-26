#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_calc
----------------------------------

Tests for `calc` module.
"""

import pytest
from calc import calc


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

def test_add_two_numbers():
    """Adds Two Numbers
    """
    c = calc.Calc()
    res = c.add(4, 5)
    assert res == 9


def test_add_three_numbers():
    """Add Three Numbers
    """
    assert calc.Calc().add(10, 20, 30) == 60

def test_add_arguments_are_int():
    """Add Method Arguments should be int
    even if someone passes string throw TypeError
    """
    with pytest.raises(TypeError):
        calc.Calc().add(10, '20', '30')