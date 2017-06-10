def insertion_sort(a):
    """
    Insertion sort
    :param a: list
    :return: list
    """
    if not a or len(a) <= 1:
        return
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while a[i] > key and i >= 0:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    return a


def selection_sort(a):
    """
    Selection sort
    :param a: list
    :return: list
    """
    if not a or len(a) <= 1:
        return
    for i in range(len(a)):
        p = i
        for j in range(i + 1, len(a)):
            if a[j] < a[p]:
                p = j
        a[p], a[i] = a[i], a[p]  # swap a[p], a[i]
    return a


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = int(len(a) / 2)
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)


def merge(left, right):
    """
    The merge method takes in the two sub arrays and creates a output array
    :param left:
    :param right:
    :return:
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):  # iterator through both arrays and arrange the elements in sorted order
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # The loop may break before all elements are copied hence append the remaining elements
    result += left[i:]
    result += right[j:]
    return result


def bubble_sort(a):
    if not a or len(a) <= 1:
        return a
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def quick_sort(a):
    pass


if __name__ == '__main__':
    arr = [5, 2, 4, 6, 1, 3]

    print(selection_sort(arr))
