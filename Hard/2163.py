import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        A_sum = [0] * (3 * n + 1)
        B_sum = [0] * (3 * n + 1)
        
        heap = []
        s = 0
        for j in range(n):
            s += nums[j]
            heapq.heappush(heap, -nums[j])
        A_sum[n] = s
        
        for i in range(n + 1, 2 * n + 1):
            x = nums[i - 1]
            if heap and x < -heap[0]:
                top_neg = heapq.heappop(heap)
                s = s - (-top_neg) + x
                heapq.heappush(heap, -x)
            else:
                pass
            A_sum[i] = s
        
        heap = []
        s = 0
        for j in range(2 * n, 3 * n):
            s += nums[j]
            heapq.heappush(heap, nums[j])
        B_sum[2 * n] = s
        
        for i in range(2 * n - 1, n - 1, -1):
            x = nums[i]
            if heap and x > heap[0]:
                top = heapq.heappop(heap)
                s = s - top + x
                heapq.heappush(heap, x)
            else:
                pass
            B_sum[i] = s
        
        ans = float('inf')
        for i in range(n, 2 * n + 1):
            diff = A_sum[i] - B_sum[i]
            if diff < ans:
                ans = diff
        return ans
