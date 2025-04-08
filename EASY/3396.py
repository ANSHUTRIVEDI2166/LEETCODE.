class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        k = 0

        while len(nums) != len(set(nums)):
            nums = nums[3:]
            k += 1
        return k

        
