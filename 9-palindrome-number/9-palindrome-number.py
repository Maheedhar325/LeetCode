class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = str(x)[::-1]
        if x>=0 and rev == str(x):
            return True
        else:
            return False
        
        