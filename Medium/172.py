class Solution(object):
    def trailingZeroes(self, n):
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        
        ans = str(fact)
        count = 0
        for j in range(len(ans) - 1, -1, -1):
            if ans[j] == '0':
                count += 1
            else:
                break
        
        return count
