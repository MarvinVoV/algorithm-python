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
        temp = a[p]
        a[p] = a[i]
        a[i] = temp
    return a


arr = [5, 2, 4, 6, 1, 3]
selection_sort(arr)
print(arr)
