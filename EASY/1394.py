class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        
        freq = Counter(arr)  # Count frequency
        max_lucky = -1

        for num, count in freq.items():
            if num == count:
                max_lucky = max(max_lucky, num)

        return max_lucky
