class Solution:
    def trap(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_left, max_right = heights[l], heights[r]
        res = 0
        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, heights[l])
                res += max_left - heights[l]
            else:
                r -= 1
                max_right = max(max_right, heights[r])
                res += max_right - heights[r]
                
        return res