def insertion_sort(a):
    """
    Insertion sort
    :param a: list
    :return: void
    """
    if not a or len(a) <= 1:
        return
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while a[i] > key and i >= 0:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key


arr = [5, 2, 4, 6, 1, 3]
insertion_sort(arr)
print(arr)
