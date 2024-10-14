""""Exercise 4, working with lists"""

__author__ = "730661650"


def all(list: list[int], value: int) -> bool:
    # return false if there are not any items in the list
    if len(list) == 0:
        return False
    # need a for statement to iterate through all items
    # if the index we are on is not equal to the integer, should return false
    # let the variable be named x, if x =! value, false
    for x in list:
        if x != value:
            return False

    return True


def max(list: list[int]) -> int:
    # raise error if there are no items in the list
    if len(list) == 0:
        raise ValueError("max() arg is an empty list")
    # we should iterate through each item in the list, if the item is greater than the initial value, that item becomes the new value
    # let the variable = x, if x is greater than the initial value (first number), it becomes the new number to compare to
    value = list[0]
    for x in list:
        if x > value:
            value = x

    return value


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    # first we have to make sure they are same lengths, len1 = len2
    if len(list_1) != len(list_2):
        return False
    # let i be the variable, iterate through each time
    # how can we write the first statement??? do we need range
    # for i in range...
    for i in range(len(list_1)):
        if list_1[i] != list_2[i]:
            return False

    return True


def extend(a: list[int], b: list[int]) -> None:
    # very simple, let's let x be the variable
    # use append to mutate a so that it has all variables from a and b
    for x in b:
        a.append(x)
