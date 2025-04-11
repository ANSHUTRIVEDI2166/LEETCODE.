class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = list(str(x))          
        reversed_lst = lst[::-1]    
        return lst == reversed_lst 
