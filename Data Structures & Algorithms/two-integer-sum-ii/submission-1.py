class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        
        while start < end:
            findingNum = target - numbers[end]
            print(findingNum)
            while numbers[start] <= findingNum:
                if findingNum == numbers[start]:
                    return [start + 1, end + 1]
                else:
                    start += 1
            end -= 1
        
        return []