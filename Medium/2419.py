class Solution:
    def longestSubarray(self, nums):
        length = 0
        ans = 0
        max_val = max(nums)
        
        for num in nums:
            if num == max_val:
                length += 1
                ans = max(ans, length)
            else:
                length = 0
        return ans
