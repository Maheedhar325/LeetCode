class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping={}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in mapping:
                return [mapping[diff],i]
            else:
                mapping[n] = i
            
                
                
        