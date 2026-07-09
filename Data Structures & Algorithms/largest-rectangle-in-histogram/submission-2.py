class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (index, current area of the rectangle at that index)

        for i in range (len(heights)):
            if not stack: 
                stack.append((i, heights[i]))
                continue

            if heights[i - 1] < heights[i]: # ascending
                stack.append((i, heights[i]))
            if heights[i - 1] == heights[i]:
                former = stack.pop()
                stack.append((i, heights[i] + former[1]))
            if heights[i - 1] > heights[i]: # descending
                count = 0
                while stack and stack[-1][1] > heights[i]:
                    temp = stack.pop()
                    max_area = max(max_area, temp[1] + heights[temp[0]] * count)
                    count += 1
                stack.append((i, heights[i] + (heights[i] * count)))
        
        count = 0
        while stack:
            temp = stack.pop()
            max_area = max(max_area, temp[1] + heights[temp[0]] * count)
            count += 1
            
        return max_area