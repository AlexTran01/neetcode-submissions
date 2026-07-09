class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (index, current area of the rectangle at that index)

        for i in range (len(heights)):
            # print(stack, "stack before run")
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
                    # print(temp, "temp")
                    # print(temp[1] + heights[temp[0]] * count, " compare area")
                    max_area = max(max_area, temp[1] + heights[temp[0]] * count)
                    # print(max_area, "max area")
                    count += 1
                # print(count)
                last_smaller_column_index = i if not stack else (i - stack[-1][0] - 1)

                stack.append((i, heights[i] + (heights[i] * last_smaller_column_index)))
            # print(stack, "stack")
            # print('\n')
        count = 0
        while stack:
            temp = stack.pop()
            max_area = max(max_area, temp[1] + heights[temp[0]] * count)
            count += 1
            
        return max_area
