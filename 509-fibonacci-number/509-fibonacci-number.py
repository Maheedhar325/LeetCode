class Solution:
    def fib(self, n: int) -> int:
        q,w = 0,1
        i = 0
        while i < n:
            z = q+w
            q = w
            w = z
            i+=1
        return q
        