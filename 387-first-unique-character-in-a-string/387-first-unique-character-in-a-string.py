class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_cnt = Counter(s)
        for i,c in enumerate(s):
            if char_cnt[c] == 1:
                return i
        return -1
        