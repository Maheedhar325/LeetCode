class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        # left,right = 0, len(nums) - 1
        # while left < right:
        #     total = nums[left] + nums[right]
        #     if total == target:
        #         return [left,right]
        #     elif total>target:
        #         right = right - 1
        #     else:
        #         left = left - 1
        mapping = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in mapping:
                return [mapping[diff],i]
            else:
                mapping[n] = i
#         nums.sort()
#         for i in range(len(nums)):
#             l = i
#             r = len(nums) - 1
#             while l<r:
#                 total = nums[l] + nums[r]
#                 if total == target:
#                     return [l,r]
#                 elif total > target:
#                     r -= 1
#                 else:
#                     l+=1
                    
                    
            
                
                
        