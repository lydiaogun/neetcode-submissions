class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #the left pointer is our bottleneck so height = min(l,r)
        left = 0
        right = len(heights) -1

        res = 0
        while left < right:
            width = right - left
            height = min(heights[right], heights[left])
            curMax = width * height
            res = max(res, curMax)

            
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return res

