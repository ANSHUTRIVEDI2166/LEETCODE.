class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return any(i in 'aeiou' for i in s)
        # If there is even a single vowel in the string, Alice Wins!!!
