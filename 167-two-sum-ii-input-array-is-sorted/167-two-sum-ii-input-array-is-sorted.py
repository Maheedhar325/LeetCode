class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping ={}
        for i,n in enumerate(numbers):
            difference = target - n
            if difference in mapping:
                return [mapping[difference]+1,i+1]
            else:
                mapping[n] = i
        
        