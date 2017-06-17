import math


def find_maximum_sub_array(a, low, high):
    """
    Find maximum sub array problem
    :param a: 
    :param low: 
    :param high: 
    :return: 
    """
    if low == high:
        return low, high, a[low]  # base case: only one element
    mid = int((low + high) / 2)
    left_low, left_high, left_sum = find_maximum_sub_array(a, low, mid)
    right_low, right_high, right_sum = find_maximum_sub_array(a, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_sub_array(a, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def find_max_crossing_sub_array(a, low, mid, high):
    sum, max_left, max_right = 0, -1, -1
    left_sum, right_sum = -math.inf, -math.inf
    for i in reversed(range(low, mid + 1)):
        sum += a[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += a[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum


if __name__ == '__main__':
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_maximum_sub_array(arr, 0, len(arr) - 1))
