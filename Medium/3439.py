class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n: int = len(startTime)
        segments: list[int] = []
        segments.append(startTime[0])
        for i in range(n - 1):
            segments.append(startTime[i + 1] - endTime[i])
        segments.append(eventTime - endTime[-1])
        output: int = 0
        window_sum: int = 0
        for i in range(k): window_sum += segments[i]
        for i in range(k, n + 1):
            if i > k: window_sum -= segments[i - k - 1]
            window_sum += segments[i]
            output = max(output, window_sum)
        return output
