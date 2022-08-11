class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        add = {}
        for i in range(len(nums)):
            if nums[i] not in add:
                add[nums[i]] = i 
            else:
                return nums[i]
        
        