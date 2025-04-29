class Solution(object):
    def countSubarrays(self, nums, k):
        target = max(nums)
        count = 0
        for i in range(len(nums)):
            count_max_number = 0
            for j in range(i,len(nums)):
                if nums[j] == target:
                    count_max_number += 1
                if count_max_number >= k:
                    count += 1
        return count
