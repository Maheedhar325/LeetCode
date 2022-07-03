class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        count = 0
        for x in range(len(s)):
            if x+1<len(s) and dictionary[s[x]] < dictionary[s[x+1]]:
                count -= dictionary[s[x]]
            else:
                count += dictionary[s[x]]
        return count
                
            
            
        
        