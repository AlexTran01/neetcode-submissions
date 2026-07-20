class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        ## LinkedList Cycle
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        ## Floyd algorithm
        second_slow = 0
        while slow != second_slow:
            slow = nums[slow]
            second_slow = nums[second_slow]
        
        return slow