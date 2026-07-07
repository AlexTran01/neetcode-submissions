class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (index, height of the rectangle at that index)

        for i in range (len(heights)):
            if not stack: 
                stack.append((i, heights[i]))
                continue

            if heights[i] > heights[i-1]: # Ascending
                stack.append((i, heights[i]))

            if heights[i] <= heights[i - 1]: # Descending / Equal
                last_index = 0
                while stack and stack[-1][1] >= heights[i]:
                    index, h = stack.pop()
                    max_area = max(max_area, h * (i-index))
                    last_index = index
        
                stack.append((last_index, heights[i]))
            
        while stack:
            i, h = stack.pop()
            max_area = max(max_area, h * (len(heights) - i))
         
        return max_area
