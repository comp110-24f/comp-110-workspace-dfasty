"""Working with Lists"""

__author__ = "730661650"


def only_evens(input_list: list[int]) -> list[int]:
    # lets define an empty list to add even values to, as we will not be mutating the list
    evens = []
    for x in input_list:
        # to test for evens, we can use remainder and ensure that if the value is divided by 2 the remainder is 0
        if x % 2 == 0:
            # use append to add the value if it is even
            evens.append(x)
    return evens


def sub(input_list_1: list[int], start: int, end: int) -> list[int]:
    # we can let the first variable be equal to 0 if it is less than zero, and the end variable be equal to the length of the list if it is greater
    if start < 0:
        start = 0
    if end > len(input_list_1):
        end = len(input_list_1)
    # create a variable for new list as again, we are not mutating the original parameter
    final_list = []
    # add all values to the new list for which the index is in the range of the two given values
    for i in range(start, end):
        if i < len(input_list_1):
            final_list.append(input_list_1[i])

    return final_list


def add_at_index(input_list_2: list[int], element: int, index: int) -> None:
    # use an or statement to define the values for which the index is out of bounds
    if index < 0 or index > len(input_list_2):
        raise IndexError("Index is out of bounds for the input list")

    # we are adding an extra value here, shifting the function to make room
    # not instead of len(input_list_2) - 1, we will subtract 2 spots due to the additional value
    input_list_2.append(0)

    for i in range(len(input_list_2) - 2, index - 1, -1):
        input_list_2[i + 1] = input_list_2[i]

    input_list_2[index] = element
