def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)


def partition(a, p, r):
    x = a[r]  # pivot element
    i = p - 1
    for j in range(p, r):  # note: j from p to r - 1  and not contains r
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]  # exchange a[i] with a[j]
    a[i + 1], a[r] = a[r], a[i + 1]  # exchange a[i+1] with a[r]
    return i + 1


if __name__ == '__main__':
    arr = [2, 8, 7, 1, 3, 5, 6, 4]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
