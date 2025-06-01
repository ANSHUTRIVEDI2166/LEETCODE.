class Solution:
    def distributeCandies(self, choco, l):
        ans = 0

        for x in range(max(0, choco - 2 * l), min(choco, l) + 1):
            y_st = max(0, choco - l - x)
            y_en = min(choco - x, l)

            if y_st <= y_en:
                ans += (y_en - y_st + 1)

        return ans
