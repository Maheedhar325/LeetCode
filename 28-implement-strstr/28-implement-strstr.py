class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        ind = haystack.find(needle)
        if ind>=0:
            return ind
        else:
            return -1
        