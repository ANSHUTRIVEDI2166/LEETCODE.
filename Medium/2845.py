class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        res = 0
        for i in range(len(nums)):
            cnt = 0
            for j in range(i, len(nums)):
                if nums[j] % modulo == k:
                    cnt += 1
                if cnt % modulo == k:
                    res += 1
        return res
