"""Challenge question 3, practicing while loops"""

__author__ = "730661650"


def num_instances(phrase: str, search_char: str) -> int:
    count = 0
    index = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1

        index += 1

    return count


num_instances(phrase="whauusup", search_char="u")
num_instances(phrase="HELLoHelLohello", search_char="H")
