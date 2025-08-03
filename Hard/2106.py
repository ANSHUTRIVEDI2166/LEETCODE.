class Solution:
    def maxTotalFruits(self, fruits, startPos, k):
        n = len(fruits)
        max_total = 0
        window_sum = 0
        left = 0

        for right in range(n):
            window_sum += fruits[right][1]

            while left <= right:
                left_pos = fruits[left][0]
                right_pos = fruits[right][0]

                left_first = abs(startPos - left_pos) + (right_pos - left_pos)
                right_first = abs(startPos - right_pos) + (right_pos - left_pos)

                if min(left_first, right_first) <= k:
                    break
                else:
                    window_sum -= fruits[left][1]
                    left += 1

            max_total = max(max_total, window_sum)

        return max_total
