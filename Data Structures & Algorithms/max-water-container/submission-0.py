class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        r, l = 0, len(heights) - 1
        while r < l :
            max_area = max(max_area, (min(heights[r], heights[l])*(l-r)))
            if heights[r] < heights[l]:
                r += 1
            else:
                l -=1
        return max_area