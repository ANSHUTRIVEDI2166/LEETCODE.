class Solution(object):
    def majorityElement(self, nums):
        count = 0
        seen = None

        for i in nums:
            if count == 0:
                seen = i
            if i == seen:
                count  += 1
            else:
                count -= 1
        return seen

