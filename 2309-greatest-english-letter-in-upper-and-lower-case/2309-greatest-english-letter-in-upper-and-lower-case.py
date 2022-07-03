class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        for i in ascii_uppercase[::-1]:
            if i in s and i.lower() in s:
                return i
            
        return ""
        