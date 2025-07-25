from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Lookup table for the range [-100, 100]. Size 201.
        seen = [False] * 201
        
        max_sum = 0
        has_positive = False
        # Initialize to a value smaller than any possible number in nums.
        max_non_positive = -101 

        for num in nums:
            # Map number to index, e.g., -100 -> 0, 100 -> 200
            index = num + 100
            
            # Only process numbers we haven't seen before.
            if not seen[index]:
                seen[index] = True
                
                if num > 0:
                    max_sum += num
                    has_positive = True
                else: # num <= 0
                    max_non_positive = max(max_non_positive, num)
        
        # If we found at least one positive number, their sum is the answer.
        # Otherwise, the best we can do is the largest non-positive number.
        return max_sum if has_positive else max_non_positive
