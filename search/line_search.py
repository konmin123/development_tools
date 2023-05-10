"""Линейный (перебором) способ поиска значения в последовательности."""


def line_search(value_for_find, sequence):
    for index, value in enumerate(sequence):
        if value == value_for_find:
            return index
    return '-1'


print(line_search(9, [1, 2, 3, 4, 5, 6, 7]))

