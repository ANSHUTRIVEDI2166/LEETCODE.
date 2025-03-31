from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairs = []
        min_sum = 0
        max_sum = 0

        for i in range(len(weights) - 1):
            pairs.append(weights[i] + weights[i + 1])

        pairs.sort()

        for i in range(k - 1):
            min_sum += pairs[i]
            max_sum += pairs[-(i + 1)]

        return max_sum - min_sum
