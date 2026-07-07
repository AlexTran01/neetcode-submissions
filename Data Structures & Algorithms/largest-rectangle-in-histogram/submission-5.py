class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (index, height of the rectangle at that index)

        for i in range (len(heights)):
            # print(stack, "stack before run")
            if not stack: 
                stack.append((i, heights[i]))
                continue

            if heights[i] > heights[i-1]: # ascending
                stack.append((i, heights[i]))

            if heights[i - 1] == heights[i]:
                former = stack.pop()
                stack.append((former[0], former[1]))

            if heights[i] < heights[i - 1]: # descending
                last_index = 0
                while stack and stack[-1][1] >= heights[i]:
                    temp = stack.pop()
                    # print(temp, "temp")
                    # print(temp[1] + heights[temp[0]] * count, " compare area")
                    # print(temp[1] * (i-temp[0]))
                    max_area = max(max_area, temp[1] * (i-temp[0]))
                    last_index = temp[0]
                    # print(max_area, "max area")
                    # count += 1
                # print(count)
                # last_smaller_column_index = i if not stack else (i - stack[-1][0] - 1)

                stack.append((last_index, heights[i] ))
            # print(stack, "stack")
            # print('\n')

        # count = 0
        # print(stack)
        while stack:
            temp = stack.pop()
            # print(max_area)
            max_area = max(max_area, temp[1] * (len(heights) - temp[0]))
            # count += 1
            
        return max_area
