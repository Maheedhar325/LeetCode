class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        case1 = nums[-1] *nums[-2] *nums[-3]
        case2 = nums[0] *nums[1]*nums[-1]
        return max(case1,case2)
            
        