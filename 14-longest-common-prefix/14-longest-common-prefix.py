class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        shortest_string = min(strs,key=len)
        minlen = len(shortest_string)
        lcp = ""
        i = 0
        while i<minlen:
            char = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i]!=char:
                    return lcp
            lcp += char
                    
            i+=1
        return lcp
        