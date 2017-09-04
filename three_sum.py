def three_sum(nums):
    """
    For example, given array S = [-1, 0, 1, 2, -1, -4],
        A solution set is:
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]
    reference: https://leetcode.com/problems/3sum/description/

    :param nums:
    :return:
    """
    res = []
    nums.sort()
    print(nums)
    for i in range(len(nums) - 1):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res


s = [-1, 0, 1, 2, -1, -4]
res = three_sum(s)
print(res)
