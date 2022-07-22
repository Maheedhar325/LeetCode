class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        [nums.remove(n) for n in nums[0:] if n ==val]
        
        return len(nums)
        