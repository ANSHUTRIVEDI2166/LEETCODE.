class Solution(object):
    def lengthOfLastWord(self, s):
        lst = list(s)
        if lst[len(s)-1] == ' ':
            lst = lst[:len(s)-2]
        count = 0
        for i in range(len(lst)-1,-1,-1):
            if lst[i] != ' ':
                count += 1
            else:
                break
        return count
                    
