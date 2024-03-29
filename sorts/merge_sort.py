"""
Сортировка слиянием. O(log n)
"""


def merge_sorted(sequence):
    """
    Сортировка слиянием. Работающая с помощью дополнительной функции.
    """
    if len(sequence) == 1 or len(sequence) == 0:
        return sequence
    middle = (len(sequence) + 1) // 2
    left = merge_sorted(sequence[:middle])
    right = merge_sorted(sequence[middle:])
    return merge(left, right)


def merge(left, right):
    """
    Вспомогательная функция.
    """
    sorted_sequence = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_sequence.append(left[left_index])
            left_index += 1
        else:
            sorted_sequence.append(right[right_index])
            right_index += 1
    sorted_sequence += left[left_index:]
    sorted_sequence += right[right_index:]
    return sorted_sequence


assert merge_sorted([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
