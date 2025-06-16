class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max1=-1
        min1=nums[0]
        for i in range(1,len(nums)):
            min1=min(min1,nums[i])
            if nums[i]>min1:
                num=nums[i]-min1
                max1=max(max1,num)
        
        return max1
