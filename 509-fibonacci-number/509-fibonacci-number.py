class Solution:
    def fib(self, n: int) -> int:
        # q,w = 0,1
        # i = 0
        # while i < n:
        #     z = q+w
        #     q = w
        #     w = z
        #     i+=1
        # return q
        
        if n<2:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        