class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r, l = 0, len(numbers) - 1
        while(r < l):
            if (s := numbers[r] + numbers[l]) == target:
                return[r+1, l+1]
            elif s > target:
                l -= 1
            else:
                r += 1
        return [] 
    
    