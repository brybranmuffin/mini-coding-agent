import pytest
from binary_search import binary_search


def test_found():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2


def test_missing():
    assert binary_search([1, 2, 3, 4, 5], 6) == -1


def test_empty_list():
    assert binary_search([], 1) == -1


def test_first_element():
    assert binary_search([1, 2, 3], 1) == 0


def test_last_element():
    assert binary_search([1, 2, 3], 3) == 2


def test_unsorted_raises_value_error():
    with pytest.raises(ValueError):
        binary_search([3, 2, 1], 2)
