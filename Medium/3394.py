class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        x_intervals = [(x1, x2) for x1, _, x2, _ in rectangles]
        y_intervals = [(y1, y2) for _, y1, _, y2 in rectangles]
        return max(self._countIntervals(x_intervals),
                   self._countIntervals(y_intervals)) >= 3

    def _countIntervals(self, intervals: list[tuple[int, int]]) -> int:
        total = 0
        lastEnd = 0
        for start, end in sorted(intervals):
            if start < lastEnd:
                lastEnd = max(lastEnd, end)
            else:
                lastEnd = end
                total += 1
        return total
