class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (index, height of the rectangle at that index)

        for i in range (len(heights)):
            if not stack: 
                stack.append((i, heights[i]))
                continue

            if heights[i] > heights[i-1]: # ascending
                stack.append((i, heights[i]))

            # if heights[i - 1] == heights[i]:
            #     former = stack.pop()
            #     stack.append((former[0], former[1]))

            if heights[i] <= heights[i - 1]: # descending
                last_index = 0
                while stack and stack[-1][1] >= heights[i]:
                    temp = stack.pop()
                    max_area = max(max_area, temp[1] * (i-temp[0]))
                    last_index = temp[0]
        
                stack.append((last_index, heights[i] ))
            
       
        while stack:
            temp = stack.pop()
            max_area = max(max_area, temp[1] * (len(heights) - temp[0]))
         
            
        return max_area
