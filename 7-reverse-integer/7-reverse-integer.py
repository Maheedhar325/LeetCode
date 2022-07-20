class Solution:
    def reverse(self, x: int) -> int:
        low = -2**31
        high = 2**31 -1
        a = abs(x)
        a = str(a)[::-1]
        if x<0 and -int(a)>low:
            return -int(a)
        elif int(a)<high:
            return int(a)
        else:
            return 0
        
        