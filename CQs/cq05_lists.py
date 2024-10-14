"""Mutating functions."""

__author__ = "730661650"


def manual_append(list_1: list[int], value: int) -> None:
    list_1.append(value)


def double(list_2: list[int]) -> None:
    idx: int = 0
    while idx < len(list_2):
        list_2[idx] *= 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
