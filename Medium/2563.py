import bisect

class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        cn = 0
        for i in range(len(nums)):
            l = bisect.bisect_left(nums, lower - nums[i], i + 1)
            r = bisect.bisect_right(nums, upper - nums[i], i + 1)
            cn += r - l
        return cn
