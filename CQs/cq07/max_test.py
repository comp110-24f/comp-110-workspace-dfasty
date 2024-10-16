"""Unit Testing For Max"""

__author__ = "730661650"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_return_value() -> None:
    """Testing that find_and_remove_max returns the expected maximum value."""
    a: list[int] = [10, 20, 5, 20]
    assert find_and_remove_max(a) == 20


def test_find_and_remove_max_mutation() -> None:
    """Testing that find_and_remove_max removes all instances of the maximum value."""
    a: list[int] = [1, 3, 3, 2]
    find_and_remove_max(a)
    assert a == [1, 2]


def test_find_and_remove_max_edge_case_empty_list() -> None:
    """Testing find_and_remove_max on an empty list."""
    a: list[int] = []
    assert find_and_remove_max(a) == -1
    assert a == []
