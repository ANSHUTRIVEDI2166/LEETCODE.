from collections import defaultdict

class Solution(object):
    def countGood(self, nums, k):
        left = 0
        count = 0
        freq = defaultdict(int)
        pairs = 0

        for right in range(len(nums)):
            pairs += freq[nums[right]]
            freq[nums[right]] += 1

            while pairs >= k:
                count += len(nums) - right
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1

        return count
