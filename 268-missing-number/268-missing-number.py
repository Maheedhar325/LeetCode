class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # count = 0
        # for i in range(len(nums) + 1):
        #     if count in nums:
        #         count = count + 1
        #         continue
        #     else:
        #         return count
        
        c = Counter(nums)
        n = len(nums)
        for i in range(n+1):
            if i not in c:
                return i
            
        