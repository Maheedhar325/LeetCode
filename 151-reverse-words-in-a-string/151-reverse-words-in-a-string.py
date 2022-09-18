class Solution:
    def reverseWords(self, s: str) -> str:
        l1 = s.split()
        l2 = []
        return " ".join(l1[::-1]).strip()
            
            
        