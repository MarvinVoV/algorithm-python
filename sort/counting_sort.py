def counting_sort(a):
    b = [None] * len(a)
    c = [0] * len(a)  # let c[0..k] be a new array. let k = len(a) and initial array a with zeros
    for j in range(len(a)):
        c[a[j]] = c[a[j]] + 1
    # c[j] now contains the number of elements equals to i.
    for i in range(1, len(c)):
        c[i] = c[i] + c[i - 1]
    # c[i] now contains the number of elements less than or equal to i.
    for j in reversed(range(len(a))):
        b[c[a[j]] - 1] = a[j]  # note: array b index based 1
        c[a[j]] = c[a[j]] - 1
    return b


if __name__ == '__main__':
    arr = [2, 5, 3, 0, 2, 3, 0, 3]
    result = counting_sort(arr)
    print(result)
