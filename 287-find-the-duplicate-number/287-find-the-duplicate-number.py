class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        add = {}
        for i in range(len(nums)):
            if nums[i] not in add:
                add[nums[i]] = i 
            else:
                return nums[i]
        
        # add = []
        # for i in range(len(nums)):
        #     if nums[i] not in add:
        #         add.append(nums[i])
        #     else:
        #         return nums[i]        
        