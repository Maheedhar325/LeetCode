class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        beg,end = 0,len(height)-1
        while beg<end:
            area = (end-beg)*min(height[beg],height[end])
            res = max(res,area)
            if height[beg]>=height[end]:
                end-=1
            else:
                beg+=1
        return res
        