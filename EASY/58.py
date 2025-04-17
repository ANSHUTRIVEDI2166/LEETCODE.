class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                count += 1
            else:
                break
        return count
                    
