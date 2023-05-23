"""
Бинарный поиск
"""


def binary_search_iterative(sequence: list, target: int):
    """Итеративная версия бинарного поиска"""
    left = 0
    right = len(sequence) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == sequence[mid]:
            return mid
        elif target < sequence[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return None


def binary_search_rek(sequence: list, target: int, left: int, right: int):
    """Рекурсивная версия бинарного поиска"""
    if left > right:
        return None
    mid = (left + right) // 2
    if sequence[mid] == target:
        return mid
    elif sequence[mid] < target:
        return binary_search_rek(sequence, target, mid + 1, right)
    else:
        return binary_search_rek(sequence, target, left, mid - 1)


if __name__ == '__main__':
    arr = [i for i in range(1, 101)]
    assert binary_search_iterative(arr, 100) == 99
    assert binary_search_rek(arr, 100, 0, len(arr) - 1) == 99

