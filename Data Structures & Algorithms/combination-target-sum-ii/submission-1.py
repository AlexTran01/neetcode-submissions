class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        counts = dict()
        for e in candidates:
            counts[e] = counts.get(e, 0) + 1

        candidates.sort() # this is the trick to put all similar elements near each others.
        res = []


        def dfs(i, total, cur):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target: 
                return

            # if counts[candidates[i]] == 0:
            #     dfs(i+1, total, cur)
            #     return

            appearCount = counts[candidates[i]]

            # include candidates[i]
            cur.append(candidates[i])
            counts[candidates[i]] -= 1
            dfs(i+1, total + candidates[i], cur)

            #exclude i
            cur.pop()
            counts[candidates[i]] += 1
            dfs(i + appearCount, total, cur)

        dfs(0, 0, [])
        return res
            
    