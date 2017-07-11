import math


def cut_rod(p, n):
    """
    递归的求解钢条切割问题
    :param p: 收益数组
    :param n: 钢条的长度
    :return:  最大收益
    """
    if n == 0:
        return 0
    q = math.inf * -1
    for i in range(0, n):
        q = max(q, p[i] + cut_rod(p, n - i - 1))
    return q


def memoized_cut_rod(p, n):
    """
    动态规划，带备忘的自顶向下法
    :param p: 收益数组
    :param n: 钢条的长度
    :return:  最大收益
    """
    r = [math.inf * - 1] * n
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n - 1] >= 0:
        return r[n - 1]
    if n == 0:
        q = 0
    else:
        q = math.inf * -1
    for i in range(0, n):
        q = max(q, p[i] + memoized_cut_rod_aux(p, n - i - 1, r))
    r[n - 1] = q
    return q


def bottom_up_cut_rod(p, n):
    """
    动态规划：自底向上法求解钢条切割问题
    :param p: 收益数组
    :param n: 钢条长度
    :return:  最大收益
    """
    r = [math.inf * -1] * (n + 1)
    r[0] = 0
    for j in range(1, n + 1):
        q = math.inf * -1
        for i in range(1, j + 1):
            q = max(q, p[i - 1] + r[j - i])
        r[j] = q

    return r[n]


if __name__ == "__main__":
    arr = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    res = cut_rod(arr, 4)
    print(res)  # 10

    res = memoized_cut_rod(arr, 4)
    print(res)

    res = bottom_up_cut_rod(arr, 4)
    print(res)
