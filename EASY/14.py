class Solution(object):
    def longestCommonPrefix(self, strs):
        count = ""

        for i in range(len(strs[0])):
            for element in strs:
                if i == len(element) or element[i] != strs[0][i]:
                    return count
            count += strs[0][i]
        return count

