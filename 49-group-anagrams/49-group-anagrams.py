class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in dict:
                dict[sorted_word] = [word]
            else:
                dict[sorted_word].append(word)
        res = []
        for items in dict.values():
            res.append(items)
        return res
        