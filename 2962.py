class Solution(object):
    def countSubarrays(self, nums, k):
        target = max(nums)
        count = 0
        target_count = 0
        i = 0

        for j in range(len(nums)):
            if nums[j] == target:
                target_count += 1

            while target_count >= k:
                if nums[i] == target:
                    target_count -= 1
                i += 1

            count += i

        return count
