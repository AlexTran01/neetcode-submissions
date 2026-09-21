class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def bfs(i, cur):
            # res.append(cur.copy())

            if i >= len(nums):
                res.append(cur.copy())
                return


            # include nums[i]
            cur.append(nums[i])
            bfs(i+1, cur)

            # exclude nums[i]
            cur.pop()
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            bfs(i+1, cur)

        bfs(0, [])
        return res
