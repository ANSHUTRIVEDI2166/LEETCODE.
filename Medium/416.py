class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        
        t = sum(nums)//2
        dp = set()
        dp.add(0)

        for i in range(len(nums) -1,-1,-1):
            copy_dp = set()
            for j in dp:
                copy_dp.add(j+nums[i])
                copy_dp.add(j)
            dp = copy_dp
        return True if t in dp else False

        
