class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(num < k for num in nums):
            return -1

        count = 0
        nums_set = set(nums)
        nums_list = list(nums_set)
        for i in range(len(nums_list)):
            if nums_list[i] > k:
                count += 1
        return count

        
