class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp = nums[i]*nums[i]
            res.append(temp)
        return sorted(res)
        