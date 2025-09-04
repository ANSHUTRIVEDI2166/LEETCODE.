class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res = 0

        # Sort points by x in increasing order and y in decreasing order
        points.sort(key=lambda point: (point[0], -point[1]))

        n = len(points)

        for i in range(n):
            xi, yi = points[i]
            curr_max_y = float('-inf')  # To keep track of the highest y seen in valid pairs

            for j in range(i + 1, n):
                xj, yj = points[j]

                # Check if point[i] is to the top-left of point[j]
                if xi <= xj and yi >= yj:
                    # Ensure we don't count duplicate y's (only count new max y)
                    if yj > curr_max_y:
                        res += 1
                        curr_max_y = yj

        return res
