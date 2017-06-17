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
