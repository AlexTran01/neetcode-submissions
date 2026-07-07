class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # indexes
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temp :
                    i_lower_temp = stack.pop()
                    res[i_lower_temp] = i - i_lower_temp

                stack.append(i)
        return res
