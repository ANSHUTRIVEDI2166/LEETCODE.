class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            digits = 0
            while num > 0:
                digits += 1
                num = num // 10
            if digits % 2 == 0:
                count += 1
        return count
