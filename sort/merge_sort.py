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


if __name__ == '__main__':
    arr = [5, 2, 4, 6, 1, 3]

    print(merge_sort(arr))
