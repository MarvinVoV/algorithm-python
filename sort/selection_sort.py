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
