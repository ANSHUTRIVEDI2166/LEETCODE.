from typing import List
from collections import Counter

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        count = Counter()
      
        
        for index, value in nums1 + nums2:
            
            count[index] += value
      
        
        return sorted(count.items())
