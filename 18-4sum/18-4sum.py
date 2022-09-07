class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        n = len(nums)
        if n<=3: return []
        for i in range(0,n-3):
            for j in range(i+1,n-2):
                curr_max = nums[i] + nums[j] + nums[-1] + nums[-2]
                curr_min = nums[i] + nums[j] + nums[j+1] + nums[j+2]
                if not curr_min<= target<= curr_max:
                    continue
                
                l,r = j+1 , n-1
                while l<r:
                    curr_sum = nums[i] + nums[j] + nums[l] +nums[r]
                    if curr_sum>target:
                        r-=1
                    elif curr_sum<target:
                        l+=1
                    else:
                        if not [nums[i],nums[j],nums[l],nums[r]] in res:
                            res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
        return res
        