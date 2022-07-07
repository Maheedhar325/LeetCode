class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dictionary = {')':'(','}':'{',']':'['}
        opening_brackets = ['(','{','[']
        
        for i in s:
            if i in opening_brackets:
                stack.append(i)
            elif stack and stack[-1] == dictionary[i]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True
        