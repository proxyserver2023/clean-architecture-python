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
	assert calc.Calc().div(10, 3) == pytest.approx(3.333333)

def test_division_with_zero_raises_exception():
	with pytest.raises(ZeroDivisionError):
		calc.Calc().div(10, 0)


"""Average Tests
"""

def test_avg_takes_iterable_and_computes_the_average():
	assert calc.Calc().avg(*(range(1,11))) == pytest.approx(5.5)


def test_avg_arguments_should_not_be_greater_than_optional_upper_threshold():
	assert calc.Calc().avg(*(range(1,11)), 1000, 2000, ut=100) == pytest.approx(5.5)


def test_avg_arguments_should_not_be_lower_than_optional_lower_threshold():
	assert calc.Calc().avg(*(range(1,11)), lt=3) == pytest.approx(6.5)

def test_avg_upper_threshold_are_included():
	assert calc.Calc().avg(*(range(1,11)), 98, ut=98) == pytest.approx(13.909090)

def test_avg_lower_threshold_are_included():
	assert calc.Calc().avg(*(range(1,11)), lt=1) == pytest.approx(5.5)

def test_avg_should_return_zero_on_empty_sequence():
	assert calc.Calc().avg() == 0

def test_avg_works_with_no_arguments():
	assert calc.Calc().avg() == 0

def test_avg_works_if_empty_list_after_outlier_removal():
	assert calc.Calc().avg(12, 98, lt=15, ut=95) == 0

def test_avg_outlier_removal_works_even_if_the_list_empty():
	assert calc.Calc().avg(12, 98, lt=15, ut=95) == 0
