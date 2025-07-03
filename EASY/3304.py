class Solution:
    def kthCharacter(self, k: int) -> str:
        # Step 1: Find the minimum level such that 2^level >= k
        level = 0
        while (1 << level) < k:
            level += 1

        # Step 2: Start recursive helper to find k-th character at that level
        def helper(k, level):
            # Step 3: Base case — level 0 string is just "a"
            if level == 0:
                return 'a'

            # Step 4: Length of first half
            half = 1 << (level - 1)  

            if k <= half:
                # Step 5: If in the first half, same position in previous level
                return helper(k, level - 1)
            else:
                # Step 6: If in second half, shift the result from first half
                ch = helper(k - half, level - 1)
                
                # Step 7: Shift character
                return chr(((ord(ch) - ord('a') + 1) % 26) + ord('a'))  

        return helper(k, level)
