class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = maxsum = nums[0]
        for i in nums[1:]:
            currsum = max(currsum+i,i)
            maxsum = max(maxsum,currsum)
        return maxsum
        