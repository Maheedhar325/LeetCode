class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping = {}
        for i,n in enumerate(nums):
            if n in mapping:
                mapping[n]+=1
            else:
                mapping[n] = 1
        return max(mapping.items(),key= operator.itemgetter(1))[0]
        
        