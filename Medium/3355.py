class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        for l, r in queries:
            for i in range(l, r+1):
                if nums[i] > 0:
                    nums[i] -= 1
        for x in nums:
            if x != 0:
                return False
        return True
