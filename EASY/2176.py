class Solution(object):
    def countPairs(self, nums, k):
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and (i*j) % k == 0:
                    count += 1
                else:
                    count += 0
        
        return count
                    
                
            

        
