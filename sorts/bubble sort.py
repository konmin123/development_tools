"""
Сортировка пузырьком, класический алгоритм с асимптотической сложностью n**2,
особенности: inplace, устойчивая.
"""


def bubble_sort(seq: list) -> list:
    """
    Сортирует последовательность.
    """
    for position in range(len(seq) - 1):
        for index in range(len(seq) - position - 1):
            if seq[index] > seq[index + 1]:
                seq[index], seq[index + 1] = seq[index + 1], seq[index]
    return seq


if __name__ == '__main__':
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([]) == []
    assert bubble_sort([9, 1]) == [1, 9]
    assert bubble_sort(['d', 'c', 'b', 'a']) == ['a', 'b', 'c', 'd']
