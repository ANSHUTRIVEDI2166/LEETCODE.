class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count = 0
        for x in range(low, high + 1):
            y = str(x)
            if len(y) % 2 != 0:
                continue
            s1 = 0
            s2 = 0
            for j in range(len(y) // 2):
                s1 += int(y[j])
                s2 += int(y[-(j + 1)])
            if s1 == s2:
                count += 1
        return count
