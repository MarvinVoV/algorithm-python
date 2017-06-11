def heap_sort(a):
    heap_size = build_max_heap(a)
    for i in reversed(range(1, len(a))):
        a[i], a[0] = a[0], a[i]  # exchange a[i] with a[1]
        heap_size -= 1
        max_heapify(a, 0, heap_size)
    return a


def build_max_heap(a):
    """
    Elements in A[n/2 + 1 .. n] are node elements. we should invoke max_heapify to adjust other elements.
    :param a: 
    :return: 
    """
    heap_size = len(a)
    for i in reversed(range(int(len(a) / 2))):
        max_heapify(a, i, heap_size)
    return heap_size


def max_heapify(a, i, heap_size):
    l = 2 * i + 1  # left node index. i based 0
    r = 2 * (i + 1)  # right node index
    largest = i
    if l < heap_size and a[l] > a[i]:
        largest = l

    if r < heap_size and a[r] > a[largest]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]  # exchange a[i] with a [largest]
        max_heapify(a, largest, heap_size)


if __name__ == '__main__':
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(heap_sort(arr))
