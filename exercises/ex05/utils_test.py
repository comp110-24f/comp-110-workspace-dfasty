"""List Unit Testing"""

__author__ = "730661650"

# first we need to import all of the functions from the other file
from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index


def test_only_evens_return_value() -> None:
    """Testing that only_evens returns only the even values of a list"""
    # let some variable be equal to the tested function, because the function is not actually being mutated
    # we must define a list and assert that the tested list returns all even values
    input_list: list[int] = [1, 4, 6, 8, 9]
    x = only_evens(input_list)
    assert x == [4, 6, 8]


# very easy, we should test that a function with all odds does not return any values
def test_only_evens_all_odds() -> None:
    """Tests that the function returns an empty list when given a list of all odds"""
    input_list: list[int] = [1, 3, 5, 7, 9]
    x = only_evens(input_list)
    # no values = [] for assertion
    assert x == []


def test_only_evens_no_mutation() -> None:
    """Tests that the function does not mutate the input_list"""
    input_list: list[int] = [1, 3, 5]
    only_evens(input_list)
    # we should assert here that although the function should return [], input list has not changed
    assert input_list == [1, 3, 5]


def test_sub_return_value() -> None:
    """Tests that sub returns the correct sublist"""
    input_list_1: list[int] = [10, 20, 30, 40]
    x = sub(input_list_1, 1, 3)
    assert x == [20, 30]


def test_sub_edge_case() -> None:
    input_list_1: list[int] = [10, 20, 30, 40]
    x = sub(input_list_1, -1, 6)
    # assert here that the result of calling the function will be the same as the original list in the case the index is out of bounds
    assert x == [10, 20, 30, 40]


def test_sub_no_mutation() -> None:
    """Testing that sub does not mutate the input list"""
    input_list_1: list[int] = [10, 20, 30, 40]
    sub(input_list_1, 1, 3)
    assert input_list_1 == [10, 20, 30, 40]


def test_add_at_index_mutation() -> None:
    """Testing that add_at_index does mutate the input list, and does so correctly"""
    input_list_2: list[int] = [1, 2, 3, 5]
    add_at_index(input_list_2, 4, 3)
    assert input_list_2 == [1, 2, 3, 4, 5]


def test_add_at_index_edge_case() -> None:
    """Tests that add_at_index raises an IndexError for an out of bounds Index"""
    input_list_2: list[int] = [1]
    # let index_out_of_bounds be an index with a value that is outside the scope of the list
    index_out_of_bounds = 2
    # original value of the boolean should be False
    raised_error = False
    # we can use "try here"
    # must have a boolean, assert that raised_error is true
    try:
        add_at_index(input_list_2, 2, index_out_of_bounds)
    except IndexError:
        raised_error = True
    assert raised_error is True


def test_add_at_index_insert_at_end() -> None:
    """Testing adding an element at the end of the list"""
    input_list_2: list[int] = [1, 2]
    add_at_index(input_list_2, 3, 2)
    assert input_list_2 == [1, 2, 3]
