class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = []
        s=""
        res=[]
        for i in digits:
            s += str(i)
        st = int(s) + 1
        for i in str(st):
            res.append(i)
        return res