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



"""Addition Tests
"""


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


def test_add_any_number_of_arguments():
	args = range(100)
	assert calc.Calc().add(*args) == 4950


"""Subtraction Tests
"""


def test_subtraction():
	assert calc.Calc().sub(10, 5) == 5


def test_subtraction_args_are_int_if_not_raise_typeerror():
	with pytest.raises(TypeError):
		calc.Calc().sub('10', 5)


"""Multiplication Tests
"""


def test_multiplication():
	assert calc.Calc().mul(*(range(1, 100))) == 933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862536979208272237582511852109168640000000000000000000000

def test_multiplication_arg_if_zero_should_raise_value_error():
	with pytest.raises(ValueError):
		calc.Calc().mul(*(range(100)))


"""Division Tests
"""

def test_division():
	assert abs(calc.Calc().div(10, 3) - 3.333333) <= 0.001

def test_division_with_zero_raises_exception():
	with pytest.raises(ZeroDivisionError):
		calc.Calc().div(10, 0)
